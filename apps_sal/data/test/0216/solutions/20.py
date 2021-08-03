n = int(input())
a = [int(x) for x in input().split()]
b = []
c = []
for i in a:
    if i >= 0:
        b.append(i)
    else:
        c.append(i)
print(sum(b) - sum(c))
