M = lambda: map(int, input().split())
L = lambda: list(map(int, input().split()))
I = lambda: int(input())

n, k = M()
t = reversed(L())
p, r = [0] * (n + 2), [1] * 100001
for i, j in enumerate(t, 1): p[i], r[j] = p[i - 1] + r[j], 0
p.reverse()
print('\n'.join(map(str, (p[I()] for i in range(k)))))
