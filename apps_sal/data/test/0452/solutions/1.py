from fractions import *
p, q = map(int, input().split())
a1 = Fraction(p, q)
n = int(input())
aaa = list(map(int, input().split()))
d2 = Fraction(aaa[-1], 1)
for i in range(2, n + 1):
    d2 = 1 / d2 + aaa[-i]
#print (d2)
print("YES" if a1 == d2 else "NO")
