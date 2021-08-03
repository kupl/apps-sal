n = int(input())
a = input().split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
khat = n * [0]
ted = 0
assl = 0
khat[0] = 1
lol = [0, 0]
for i in range(1, len(khat)):
    khat[i] = max([khat[i - 1], a[i] + 1])
for i in range(len(khat) - 2, -1, -1):
    if khat[i] < khat[i + 1] - 1:
        khat[i] = khat[i + 1] - 1
    ted = ted + (khat[i] - (a[i] + 1))
ted = ted + (khat[n - 1] - (a[n - 1] + 1))
print(ted)
