from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a1 = a[::2]
a2 = a[1::2]

c = Counter(a1)
c1 = []
for i in c:
    c1.append([c[i], i])
c1.sort(reverse=True)

c = Counter(a2)
c2 = []
for i in c:
    c2.append([c[i], i])
c2.sort(reverse=True)

ans = n
if c1[0][1] != c2[0][1]:
    ans -= c1[0][0]
    ans -= c2[0][0]
else:
    buf1 = 0
    buf1 += c1[0][0]
    if len(c2) > 1:
        buf1 += c2[1][0]
    buf2 = 0
    buf2 += c2[0][0]
    if len(c1) > 1:
        buf2 += c1[1][0]
    ans -= max(buf1, buf2)
print(ans)
