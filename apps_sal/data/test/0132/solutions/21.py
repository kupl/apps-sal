n = int(input())
l = []
l = input().split()
for i in range(n):
    l[i] = int(l[i])
l.extend(l)

otv = 400
for i in range(n):
    s = 0
    j = i
    while s < 180:
        s += l[j]
        j += 1

    if abs(s - 180) * 2 < otv:
        otv = abs(s - 180) * 2
print(otv)
