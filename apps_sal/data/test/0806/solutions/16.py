n, l, r = [int(v) for v in input().split()]

m = r - l
r = (
    m // 3 + 1,
    (m - 1) // 3 + 1,
    (m - 2) // 3 + 1,
)

rem = l % 3
if rem == 0:
    r0, r1, r2 = r
elif rem == 1:
    r1, r2, r0 = r
else:
    r2, r0, r1 = r

w0, w1, w2 = r0, r1, r2
mod = 1000000007

for _ in range(1, n):
    w0, w1, w2 = (
        (w0 * r0 + w1 * r2 + w2 * r1) % mod,
        (w0 * r1 + w1 * r0 + w2 * r2) % mod,
        (w0 * r2 + w1 * r1 + w2 * r0) % mod,
    )

print(w0)
