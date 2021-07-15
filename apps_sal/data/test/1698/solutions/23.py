l = input().split()
n = int(l[0])
k = int(l[1])

l1 = input().split()
for x in range(n):
    l1[x] = int(l1[x])
l1 = sorted(l1, reverse = True)

c = 0
for x in range(0, n, k):
    c += 2*(l1[x]-1)

print(c)

