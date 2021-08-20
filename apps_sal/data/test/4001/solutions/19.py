n = int(input())
d = [int(t) for t in input().split(' ')]
d.sort()
d.reverse()
d1 = d[0]
d2 = None
for i in range(1, len(d)):
    if d1 % d[i] != 0 or d[i] == d[i - 1]:
        d2 = d[i]
        break
print(d1, d2)
