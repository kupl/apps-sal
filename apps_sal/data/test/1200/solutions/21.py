def gcd(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % a
    return a


input()
x = sorted([int(i) + 1000000001 for i in input().split()])
ans = x[1] - x[0]
for i in range(1, len(x)):
    ans = gcd(x[i] - x[i - 1], ans)
res = 0
for i in range(1, len(x)):
    res += (x[i] - x[i - 1]) // ans - 1
print(res)
