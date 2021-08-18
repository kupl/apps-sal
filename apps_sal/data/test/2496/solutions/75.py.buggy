from math import gcd
n = int(input())
l = list(map(int, input().split()))
mal = max(l)
e = [i for i in range(mal + 1)]

x = 2
while x * x <= mal:
    if x == e[x]:
        for m in range(x, len(e), x):
            if e[m] == m:
                e[m] = x
    x += 1
# print(e)
s = set()
f = 0
for i in l:
    st = set()
    while i > 1:
        st.add(e[i])
        i //= e[i]
    if not s.isdisjoint(st):
        f = 1
        break
    s |= st

if f == 0:
    print('pairwise coprime')
    return
p = l[0]
for i in range(1, n):
    p = gcd(p, l[i])
if p == 1:
    print('setwise coprime')
else:
    print('not coprime')
