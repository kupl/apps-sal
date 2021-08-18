n = int(input())
x = [int(x) for x in input().split()]
p = x[0]
l = []
for i in range(1, n):
    for a, b in l[:-1]:
        if (a < x[i] < b) ^ (a < p < b):
            print('yes')
            return
    l.append((min(p, x[i]), max(p, x[i])))
    p = x[i]
print('no')
