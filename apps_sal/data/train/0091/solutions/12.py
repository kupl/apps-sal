from collections import deque
for i in range(int(input())):
    n = int(input())
    h = deque([i+1 for i in range(n)])
    used = [False]*n
    ans = [0]*n
    c = list(map(int,input().split()))
    ans[0] = c[0]
    used[c[0]-1] = True
    f = True
    for i in range(n):
        if i+1>c[i]:
            f = False
    if not f:
        print(-1)
        continue
    for i in range(n-1):
        if c[i+1]!=c[i]:
            ans[i+1] = c[i+1]
        else:
            x = h.popleft()
            while used[x-1]:
                x = h.popleft()
            ans[i+1] = x
        used[ans[i+1] - 1] = True
    print(*ans)
