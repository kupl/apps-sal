(h1, a1, c1) = map(int, input().split())
(h2, a2) = map(int, input().split())
ans = 0
ad = []
while 1:
    ans += 1
    if h1 <= a2 and h2 > a1:
        h1 += c1
        ad.append('HEAL')
    else:
        h2 -= a1
        ad.append('STRIKE')
    if h2 <= 0:
        break
    h1 -= a2
print(ans)
for d in ad:
    print(d)
