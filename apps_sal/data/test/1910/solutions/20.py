n = int(input())
l = 2 * n - 2
s = 0
k = n
if k < l - 1:
    d1 = (l - (k + 2) + 1) * 9 * 4 ** (l - 2 - k)
else:
    d1 = 0
d2 = 2 * 3 * 4 ** (l - 1 - k)
s += d1 + d2
print(s * 4)
