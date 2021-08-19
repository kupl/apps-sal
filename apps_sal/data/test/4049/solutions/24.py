n = int(input())
(a1, a2, a3) = map(int, input().split())
(b1, b2, b3) = map(int, input().split())
c1 = a1 - (b3 + b1)
c2 = a2 - (b1 + b2)
c3 = a3 - (b2 + b3)
s = 0
if c1 > 0:
    s += c1
if c2 > 0:
    s += c2
if c3 > 0:
    s += c3
print(s, end=' ')
print(min(a1, b2) + min(a2, b3) + min(a3, b1))
