from collections import Counter


N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

a = Counter(A)
b = Counter(B)

cnt = 0
aa = 0
bb = 0
flag = False
for i in range(1,6):
    diff = a[i]-b[i]
    if diff % 2 == 1:
        flag = True
        break
    if diff > 0:
        aa += diff // 2
    else:
        bb += -diff // 2

if flag:
    print(-1)
else:
    if (aa == bb):
        print(aa)
    else:
        print(-1)


