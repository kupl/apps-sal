def gcd(x, y):
    while x:
        x, y = y % x, x
    return y


input()
*a, = map(int, input().split())
while len(a) > 1:
    x = a.pop()
    y = a.pop()
    a.append(gcd(x, y))
print(a.pop())
