i = input().split()
f1 = int(i[0])
f2 = int(i[1])

n = int(input()) % 6
l = []
for x in range(n + 6):
    l.append(0)

l[0] = f1
l[1] = f2
for x in range(2, n + 6):
    l[x] = (l[x - 1] - l[x - 2])

print(l[n - 1] % 1000000007)
