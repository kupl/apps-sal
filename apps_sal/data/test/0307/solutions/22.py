l = [int(x) for x in input().split()]
k = min(l[0], l[2], l[3])
a = l[0] - k
j = min(a, l[1])
print(256 * k + 32 * j)
