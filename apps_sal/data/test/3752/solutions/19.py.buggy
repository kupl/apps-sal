k, d, t = list(map(int, input().split()))
if k % d == 0:
    print(float(t))
    return
x = ((k // d) + 1) * d
# print(x)
y = (k + (x - k) / 2)
# print(y)
z = (t // y)
# print(z*y)
l = t - (z * y)
m = min(l, k)
l -= (m)
# print(l)
ans = (z * x + m + [0, l * 2][l > 0])
print(ans)
