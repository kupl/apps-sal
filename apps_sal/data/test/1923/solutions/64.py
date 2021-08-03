n = int(input())
l = sorted([int(x) for x in input().split(' ')])
l.reverse()
s = 0
for i in range(0, n, 1):
    s += min(l[2 * i:2 * i + 2])
print(s)
