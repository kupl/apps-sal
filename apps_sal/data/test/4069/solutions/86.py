x, k, d = input().split()
x = int(x)
k = int(k)
d = int(d)
ans = 0
if abs(x) >= abs(k * d):
    ans = abs(x) - abs(k * d)
else:
    kaisuu = int(abs(x) / d)
    k_2 = k - kaisuu
    if k_2 % 2 == 0:
        ans = abs(x) - d * kaisuu
    else:
        ans = abs((abs(x) - d * kaisuu) - abs(d))
print(int(ans))
