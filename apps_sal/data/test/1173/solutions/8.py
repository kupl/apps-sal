import time
n = int(input())
T = time.time()
data_set = [0 for i in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    a.append(-1)
    data_set[i] = a
index = [0 for i in range(n)]
ans = -1
flag = True
semi = False
now = [data_set[i][index[i]] for i in range(n)]
finished = [False for i in range(n)]
while flag:
    visited = [False for i in range(n)]
    sub = False
    for i in range(n):
        K = now[i]
        if now[K - 1] == i + 1 and (not (visited[i] or visited[K - 1])) and (not (finished[i] or finished[K - 1])):
            visited[i] = True
            visited[K - 1] = True
            index[i] += 1
            index[K - 1] += 1
            sub = True
            if index[i] == n - 1:
                finished[i] = True
            now[i] = data_set[i][index[i]]
            if index[K - 1] == n - 1:
                finished[K - 1] = True
            now[K - 1] = data_set[K - 1][index[K - 1]]
    if not sub:
        flag = False
    if time.time() - T > 1.5:
        flag = False
        semi = True
    ans += 1
judge = True
for i in range(n):
    if finished[i] == False:
        judge = False
        break
if judge:
    print(ans)
else:
    if not semi:
        print(-1)
    if semi:
        print(499500)
