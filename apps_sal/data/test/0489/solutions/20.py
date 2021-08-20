n = int(input())
l = list(map(int, input().strip().split(' ')))
l1 = sorted(l)
a = l1[0]
b = l1[1]
c = l1[2]
if a == b and b == c:
    ans = l.count(a)
    a = ans
    print(a * (a - 1) * (a - 2) // 6)
elif b != c:
    ans = l.count(c)
    c = ans
    print(c)
else:
    ans = l.count(b)
    b = ans
    print(b * (b - 1) // 2)
