n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l1 = []
for i in range(len(l)):
    if(l[i] not in l1):
        l1.insert(0, l[i])
    if(len(l1) > k):
        l1 = l1[:len(l1) - 1]
print(len(l1))
print(*l1)
