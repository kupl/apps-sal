n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
t = [0] * (n + 1)
for i in range(1, n + 1):
    t[p[i]] = i
i = 1
f = 1
ans = []
while i < n:
    if p[i] != f:
        x = t[f]
        for j in range(i, x - 1):
            if p[j] != j + 1:
                print(-1)
                return
        for j in range(i, x)[::-1]:
            ans.append(j)
        p[x] = p[x - 1]
        f = f + (x - i)
        i = x
    else:
        f += 1
        i += 1
if len(ans) != n - 1:
    print(-1)
    return
for i in ans:
    print(i)
