(n, k) = list(map(int, input().split()))
x = list(map(int, input().split()))
fpos = [k for i in range(n + 1)]
lpos = [-1 for i in range(n + 1)]
for i in range(1, k + 1):
    lpos[x[i - 1]] = i
for i in range(k, 0, -1):
    fpos[x[i - 1]] = i
ans = 0
for i in range(1, n + 1):
    if lpos[i] == -1:
        ans += 1
for i in range(1, n):
    ans += fpos[i] >= lpos[i + 1]
    ans += fpos[i + 1] >= lpos[i]
print(ans)
