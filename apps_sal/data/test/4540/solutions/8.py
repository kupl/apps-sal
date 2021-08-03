n = int(input())
l = [0] + list(map(int, input().split())) + [0]
d = [abs(a - b) for a, b in zip(l, l[1:])]
m = sum(d)
for i in range(n):
    print((m + abs(l[i] - l[i + 2]) - (d[i] + d[i + 1])))
