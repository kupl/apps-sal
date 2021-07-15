t = input
p = print
r = range
n = int(t())
a, b = 0, 0
for i in r(n):
    m, c = map(int, t().split())
    if m > c:
        a += 1
    elif m < c:
        b += 1
ans = "Mishka"
if a==b:
    ans = "Friendship is magic!^^"

if a < b:
    ans = "Chris"

p(ans)
