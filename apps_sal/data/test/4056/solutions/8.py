def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


n = int(input())
a = list(map(int, input().split()))
g = 0
for x in a:
    g = gcd(g, x)
ans = 0
t = 1
while t * t <= g:
    if g % t == 0:
        ans += 1
        if t * t != g:
            ans += 1
    t += 1
print(ans)
