(n, k, m) = list(map(int, input().split()))

d1 = {}
acc = 0
for x in input().split():
    d1[x] = acc
    acc += 1

array = []
for x in input().split():
    array.append(int(x))

mass = []
for x in range(k):
    mass.append([])

d2 = {}
for x in range(k):
    temp = list(map(int, input().split()))
    for y in temp[1:]:
        mass[x].append(array[y - 1])
        d2[y - 1] = x
    mass[x].sort()

ans = 0
for x in input().split():
    ans += mass[d2[d1[x]]][0]

print(ans)
