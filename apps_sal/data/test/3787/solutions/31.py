import sys
n, a, b = map(int, input().split())
if a + b > n + 1 or a * b < n:
    print(-1)
    return

ans = []
L = [a] * b
x = a * b - n
for i in range(1, b):
    L[i] -= min(a - 1, x)
    x -= min(a - 1, x)
L.reverse()

ct = 1
for i in range(b):
    l = []
    for j in range(L[i]):
        l.append(str(ct))
        ct += 1
    ans.append(' '.join(l))
ans.reverse()

print(' '.join(ans))
