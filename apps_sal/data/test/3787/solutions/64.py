(n, a, b) = map(int, input().split())
ans = []
L = [a] * b
x = a * b - n
ct = 1
for i in range(b - 1, 0, -1):
    y = min(a - 1, x)
    L[i] -= y
    x -= y
for i in range(b):
    l = []
    for j in range(L[i]):
        l.append(str(ct))
        ct += 1
    ans.append(' '.join(l))
ans.reverse()
print(-1 if a + b > n + 1 or a * b < n else ' '.join(ans))
