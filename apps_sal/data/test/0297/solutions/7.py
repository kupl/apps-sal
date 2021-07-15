n, m, k = list(map(int, input().split()))

if 2 * n * m % k != 0:
    print("NO")
    return

g = n
b = k

while g > 0 and b > 0:
    if g > b:
        g %= b
    else:
        b %= g

g = g + b
k1 = k // g
p = False
if k1 % 2 == 0:
    k1 //= 2
    p = True
a = n // g
b = m // k1

if not p:
    if a < n:
        a *= 2
    else:
        b *= 2

print("YES")
# print(a * b // 2, n * m // k)
print(0, 0)
print(a, 0)
print(0, b)

