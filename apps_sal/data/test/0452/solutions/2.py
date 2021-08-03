from fractions import Fraction
pq = Fraction(*map(int, input().split()))
input()
a = list(map(int, input().split()))
a.reverse()
f = Fraction(a[0], 1)
for i in a[1:]:
    f = i + Fraction(1, f)
if pq == f:
    print("YES")
else:
    print("NO")
