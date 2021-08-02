
def gcd(x, y):
    if(y == 0):
        return x
    else:
        return gcd(y, x % y)


p, q = [int(i) for i in input().split()]
n = int(input())
a = [int(i) for i in input().split()]
x, y = 1, 0
for i in a[::-1]:
    x, y = y + i * x, x
a, b = gcd(p, q), gcd(x, y)
p = p // a;
q = q // a
x = x // b
y = y // b
if x == p and y == q:
    print("YES")
else:
    print("NO")
