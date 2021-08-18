n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

s = sum(a)
i = 0
l = len(a)
while round(s / l + 0.00001) != k:
    i += 1
    s += k
    l += 1
print(i)
