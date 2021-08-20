(n, t, k, d) = [int(i) for i in input().split()]
n = (n + k - 1) // k
t0 = t * n
dt = t0 - d
ans = 'YES' if dt > t else 'NO'
print(ans)
