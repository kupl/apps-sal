from collections import Counter
n = int(input())
v = list(map(int, input().split()))
v1 = v[0::2]
v2 = v[1::2]

c1 = list(Counter(v1).items())
c2 = list(Counter(v2).items())

c1 = sorted(c1, key=lambda x: x[1], reverse=True)
c2 = sorted(c2, key=lambda x: x[1], reverse=True)

c1.append((0, 0))
c2.append((0, 0))

#print(c1[:3], c2[:3])
if c1[0][0] != c2[0][0]:
    print(n - c1[0][1] - c2[0][1])
else:
    a = c1[0][1] + c2[1][1]
    b = c1[1][1] + c2[0][1]
    if a < b:
        print(n - b)
    else:
        print(n - a)
