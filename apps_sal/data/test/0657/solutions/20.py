(a, b) = [int(i) for i in input().split()]
(x, y, z) = [int(i) for i in input().split()]
a -= 2 * x
a -= y
b -= y
b -= 3 * z
ans = 0
if a < 0:
    ans -= a
if b < 0:
    ans -= b
print(ans)
