s, b = map(int, input().split())
a = list(map(int, input().split()))
for i in range(s):
    a[i] = [a[i], i, None]
bases = []
for i in range(b):
    d, g = map(int, input().split())
    bases.append((d, g))
bases.sort()
a.sort()
j = 0
count = 0
for i in range(b):
    while j < s and a[j][0] < bases[i][0]:
        a[j][2] = count
        j += 1
    if j == s:
        break
    count += bases[i][1]
    if i == b - 1:
        if j < s and a[j][0] >= bases[i][0]:
            r = j
            for j in range(r, s):
                a[j][2] = count
a.sort(key=lambda x: x[1])
a = [x[2] for x in a]
print(*a)
