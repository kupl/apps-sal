N = int(input())
a = list(map(int, input().split()))

n4, n2 = 0, 0
for i in range(N):
    if a[i] % 4 == 0:
        n4 += 1
    elif a[i] % 2 == 0:
        n2 += 1

if n4 >= N // 2:
    print('Yes')
elif n4 * 2 + n2 >= N:
    print('Yes')
else:
    print('No')
