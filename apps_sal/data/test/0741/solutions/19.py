from itertools import accumulate
(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
a = [0] + a + [m]
d = [0] * (n + 1)
for i in range(n + 1):
    d[i] = a[i + 1] - a[i]
fwd = [0] * len(a)
s = 0
for i in range(1, len(a)):
    if i % 2 == 1:
        s += d[i - 1]
        fwd[i] = s
    else:
        fwd[i] = fwd[i - 1]
bwd = [0] * len(a)
s = 0
for i in range(1, len(a)):
    if (len(a) - 1 - i) % 2 == 0:
        s += d[-i]
        bwd[-i - 1] = s
    else:
        bwd[-i - 1] = bwd[-i]
fwd_ = list(accumulate([0] + d))
bwd_ = list(accumulate([0] + d[::-1]))[::-1]
maxx = fwd[-1]
for i in range(n + 1):
    if a[i + 1] - a[i] > 1:
        if i % 2 == 0:
            x = fwd[i] + a[i + 1] - a[i] - 1 + bwd_[i + 1] - bwd[i + 1]
        else:
            x = fwd[i] + a[i + 1] - a[i] - 1 + bwd_[i + 1] - bwd[i + 1]
        if x > maxx:
            maxx = x
print(maxx)
