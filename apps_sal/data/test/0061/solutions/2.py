(n, bx) = map(int, input().split())
s1 = 0
p1 = 1
for i in list(map(int, input().split()))[::-1]:
    s1 += i * p1
    p1 *= bx
(m, by) = map(int, input().split())
s2 = 0
p2 = 1
for i in list(map(int, input().split()))[::-1]:
    s2 += i * p2
    p2 *= by
if s1 == s2:
    print('=')
elif s1 > s2:
    print('>')
else:
    print('<')
