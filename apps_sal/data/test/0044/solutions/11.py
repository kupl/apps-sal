from sys import stdin, stdout
(d, k, a, b, t) = map(int, stdin.readline().split())
ans = 0
if k * b > k * a + t:
    if k < d:
        ans += (d // k - 1) * t + (d - d % k) * a
        d %= k
        if d * a + t < d * b:
            ans += d * a + t
        else:
            ans += d * b
    else:
        ans += a * d
elif k < d:
    ans = (d - k) * b + k * a
else:
    ans = d * a
stdout.write(str(ans))
