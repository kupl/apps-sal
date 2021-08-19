l = list(map(int, input().split()))
n = l[0]
del(l[0])
a = 0
for i in range(10**7):
    a += 1
# for i in range(n):
#   l[i] = str(l[i])
l.sort()
print(*l)
