n = int(input())
a = list(map(int, input().split()))
c = list([x for x in a if x % 2 == 0 and x > 0])
b = list([x for x in a if x % 2 != 0])
b = sorted(b, reverse=True)
mm = int(-10000000000.0)
s = 0
for i in range(len(b)):
    s += b[i]
    if i % 2 == 0:
        mm = max(mm, s)
print(sum(c) + mm)
