n = int(input())
l = [int(x) for x in input().split()]

l.sort()

l2 = [0] * n
prev = l[0]
count = 1
k = 0

for i in range(1, n):
    if l[i] != prev:
        l2[k] = [prev, count]
        k += 1
        prev = l[i]
        count = 1
    else:
        count += 1

l2[k] = [prev, count]
k += 1
for i in range(k-1, 0, -1):
    if l2[i][1] % 2 == 1 and l2[i-1][0] == (l2[i][0] - 1):
        l2[i-1][1] += 1
    l2[i][1] //= 2
l2[0][1] //= 2
i = k-1
j = k-1
res = 0
while i >= 0 and j >= 0:
    if i == j:
        res += l2[i][0] * l2[i][0] * (l2[i][1] // 2)
        l2[i][1] %= 2
        if l2[i][1] == 0:
            i -= 1
            j -= 1
        else:
            i -= 1

    else:
        if l2[i][1] == 0:
            i -= 1
            continue
        res += l2[i][0] * l2[j][0]
        l2[i][1] -= 1
        j = i

print(res)

