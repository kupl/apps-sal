np = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

l1 = [a[0]]
l2 = [a[np[0] - 1]]

for i in range(1, np[0] - 1) :
    l1.append(l1[i - 1] + a[i])
    l2.append(l2[i - 1] + a[-(i + 1)])

max = 0
for i in range(0, np[0] - 1) :
    if l1[i] % np[1] + l2[-(i + 1)] % np[1] > max:
        max = l1[i] % np[1] + l2[-(i + 1)] % np[1]

print(max)

