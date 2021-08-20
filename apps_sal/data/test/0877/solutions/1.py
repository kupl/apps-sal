(n, m) = [int(i) for i in input().split()]
s1 = [1]
s2 = [n]
for i in range(m):
    (a, b) = [int(i) for i in input().split()]
    s1.append(min(a, b))
    s2.append(max(a, b))
s1.sort()
s2.sort()
if s1[-1] < s2[0]:
    print(s2[0] - s1[-1])
else:
    print(0)
