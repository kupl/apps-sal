N = int(input())
d = list(map(int, input().split()))

d.sort()
c = int(len(d) / 2)
l = d[:c]
r = d[c:]
print((r[0] - l[-1]))

