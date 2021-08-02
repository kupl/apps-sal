from collections import deque

K = int(input())

while (K % 2 == 0):
    K = K // 2
while (K % 5 == 0):
    K = K // 5

if(K == 1): print("1")
else:
    visited = [-1 for i in range(K)]
    queue = deque([])
    st = 1

    while True:
        visited[st] = 1
        queue.append(st)
        st = (10 * st) % K
        if (st == 1): break

    while queue:
        a = queue.popleft()
        if (visited[0] != -1): break
        if (visited[(a + 1) % K] == -1):
            st = (a + 1) % K
            while True:
                visited[st] = visited[a] + 1
                queue.append(st)
                st = (10 * st) % K
                if (st == ((a + 1) % K)): break
            if (visited[0] != -1): break

    print(visited[0])
