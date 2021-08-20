(n, t, k, d) = map(int, input().split())
ans1 = (n + k - 1) // k * t
ans2 = 1 << 30
for x in range(1, 1000010):
    if ((d + x) // t + x // t) * k >= n:
        ans2 = d + x
        break
if ans1 <= ans2:
    print('NO')
else:
    print('YES')
