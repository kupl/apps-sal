from math import ceil
from math import floor

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ln = n // k
p = 1
mod = 1000000007

for i in range(ln):
    tmp = (10 ** k - 1) // a[i] + 1
    l = ceil(b[i] * (10 ** (k - 1)) / a[i])
    r = floor(((b[i] + 1) * (10 ** (k - 1)) - 1) / a[i])
    tmp -= r - l + 1
    p = (p * tmp) % mod

print(p)


