n = int(input())
l = list(map(int, input().split()))
k = l.count(1)
l1 = []
c = 1
for i in range(1, len(l)):
    if l[i] == 1:
        l1.append(c)
        c = 1
    else:
        c += 1
l1.append(c)
print(k)
print(*l1)
