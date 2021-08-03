n = int(input())
li = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        li[i][x - 1] = y

ans = 0
for i in range(2**n):
    s = 0
    t = [0] * n
    for j in range(n):
        if i >> j & 1:
            t[j] = 1
    is_contradict = 0
    for j in range(n):
        if t[j]:
            for k in range(n):
                if li[j][k] == -1:
                    continue
                if li[j][k] != t[k]:
                    is_contradict = 1
    if not is_contradict:
        ans = max(ans, sum(t))

print(ans)
