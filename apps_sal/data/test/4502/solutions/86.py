n = int(input())
la = list(map(int, input().split()))
l1 = []
l2 = []
for i in range(n):
    if i % 2 == 0:
        l1.append(la[i])
    else:
        l2.append(la[i])
if n % 2 == 0:
    for i in reversed(l2):
        print(i, end=' ')
    for i in l1:
        print(i, end=' ')
else:
    for i in reversed(l1):
        print(i, end=' ')
    for i in l2:
        print(i, end=' ')
