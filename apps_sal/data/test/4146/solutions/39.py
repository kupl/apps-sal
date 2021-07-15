from collections import Counter
n = int(input())
v = list(map(int,input().split()))
a = Counter(v[::2])
b = Counter(v[1::2])
a = a.most_common()
b = b.most_common()
a1 = a[0][1]
b1 = b[0][1]
if len(a) == 1:
    a2 = 0
else:
    a2 = a[1][1]
if len(b) == 1:
    b2 = 0
else:
    b2 = b[1][1]
if a[0][0] != b[0][0]:
    print(n-(a1+b1))
else:
    print(min(n-(a1+b2),n-(a2+b1)))
