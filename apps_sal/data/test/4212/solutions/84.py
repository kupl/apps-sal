from collections import deque

N, M, Q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(Q)]
que = deque()
for i in range(1, M + 1):
    que.append([i])
ans = 0

while que:
    check = que.popleft()
    tmp = 0
    if len(check) == N:
        for A in lst:
            if check[A[1] - 1] - check[A[0] - 1] == A[2]:
                tmp += A[3]
        ans = max(ans, tmp)
    else:
        for j in range(check[-1], M + 1):
            que.append(check + [j])

print(ans)
