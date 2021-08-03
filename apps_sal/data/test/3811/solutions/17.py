import math


def factor(n):
    q = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            q += 1
    return q


n = int(input())
temp = []
lis = []
k = 0
a1, b1 = list(map(int, input().split()))
j = 0
for i in range(2, int(math.sqrt(a1 + 1)) + 1):
    if(a1 % i == 0):
        lis.append(i)
        lis.append(a1 // i)
lis.append(a1)
for i in range(2, int(math.sqrt(b1 + 1)) + 1):
    if(b1 % i == 0):
        lis.append(i)
        lis.append(b1 // i)
lis.append(b1)
lis = list(set(lis))
p = len(lis)
for j in range(len(lis)):
    if(factor(lis[j]) == 0):
        lis.append(lis[j])
del lis[:p]
for i in range(1, n):
    a, b = list(map(int, input().split()))
    if(a == a1 or b == b1 or a == b1 or b == a1):
        a1 = a
        b1 = b
        continue
    a1 = a
    b1 = b
    l = len(lis)
    for j in range(l):
        if(a % lis[j] == 0 or b % lis[j] == 0):
            lis.append(lis[j])
    del lis[:l]
    if(len(lis) == 0):
        k = 1
        break
if(k == 0):
    print(lis[0])
else:
    print(-1)
