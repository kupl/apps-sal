N = int(input())
a = list(map(int, input().split()))
c2 = 0
c4 = 0
for i in range(N):
    if a[i] % 4 == 0:
        c4 += 1
    elif a[i] % 2 == 0:
        c2 += 1
f = c4 * 2 + 1
if f >= N or f + c2 - 1 >= N:
    print('Yes')
else:
    print('No')
