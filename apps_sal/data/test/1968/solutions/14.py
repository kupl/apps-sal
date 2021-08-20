(n, v) = map(int, input().split())
l1 = []
count = 0
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(1, l[0] + 1):
        if v > l[j]:
            count = count + 1
            l1.append(i + 1)
            break
print(count)
l1.sort()
for k in range(len(l1)):
    if len(l1) == 0:
        print('\t')
    else:
        print(l1[k], '', end='')
