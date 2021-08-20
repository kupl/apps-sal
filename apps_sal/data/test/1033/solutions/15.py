from math import ceil, sqrt
(n, H) = map(int, input().split(' '))
k = ceil(0.5 * (sqrt(8 * n + 1) - 1))
while k * k + k >= 2 * n:
    k -= 1
while k * k + k < 2 * n:
    k += 1
if k <= H:
    print(k)
else:
    k = ceil(sqrt(2 * H * H - 2 * H + 4 * n) - H)
    if (k - H) % 2 == 1:
        k += 1
    a = (k - H) // 2
    while (H + a) * (H + a + 1) + (H + a - 1) * (H + a) - (H - 1) * H >= 2 * n:
        k -= 2
        a -= 1
    while (H + a) * (H + a + 1) + (H + a - 1) * (H + a) - (H - 1) * H < 2 * n:
        k += 2
        a += 1
    m = k
    k = ceil(sqrt(2 * H * H - 2 * H + 4 * n + 1) - H - 1)
    if (k - H) % 2 == 0:
        k += 1
    a = (k - H - 1) // 2
    while (H + a) * (H + a + 1) + (H + a + 1) * (H + a) - (H - 1) * H >= 2 * n:
        k -= 2
        a -= 1
    while (H + a) * (H + a + 1) + (H + a + 1) * (H + a) - (H - 1) * H < 2 * n:
        k += 2
        a += 1
    print(max(min(m, k), H + 1))
