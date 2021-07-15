import math
a, b = map(int, input().split())
c = math.gcd(a, b)
a //= c
b //= c
ans = 0
def d(x, t):
    nonlocal ans
    while(x > 1 and x % t == 0):
        x //= t
        ans += 1
    return x
for i in [2, 3, 5]:
    a = d(a, i)
    b = d(b, i)
print([-1, ans][a == 1 and b == 1])
