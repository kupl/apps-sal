n = int(input())
a = list([int(x[1]) - x[0] - 1 for x in enumerate(input().split())])
nh = (n + 1) // 2
a.sort()
b = a[nh-1]
s = 0
for ai in a: s+= abs(ai-b)
print(s)


