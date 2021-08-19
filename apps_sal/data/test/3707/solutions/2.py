(n, t, k, d) = map(int, input().split())
ans1 = n // k
if n % k:
    ans1 += 1
ans1 *= t
if d < ans1 - t:
    print('YES')
else:
    print('NO')
