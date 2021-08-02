from fractions import gcd

n = int(input())
v = [int(x) for x in input().split()]

v.sort()


g = 0
last = v[0]
for i in v:
    if i != last:
        g = gcd(g, i - last)
        last = i


ans = (v[n - 1] - v[0]) // g - n + 1
print(ans)
