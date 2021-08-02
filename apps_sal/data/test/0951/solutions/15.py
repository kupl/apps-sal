k = int(input())
d = list(map(int, list(input())))
d.sort()
l = sum(d)
i = 0
while l < k:
    l += 9 - d[i]
    i += 1
print(i)
