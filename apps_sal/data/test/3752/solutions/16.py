(k, d, t) = list(map(int, input().split()))
off = k // d * d + d - k if k % d != 0 else 0
period = k + off
performance = off / 2 + k
part = int(t / performance)
ans = part * period
t -= part * performance
if t <= k:
    ans += t
else:
    ans += k
    t -= k
    ans += 2 * t
print(ans)
