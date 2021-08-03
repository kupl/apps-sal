N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
AM = A[0:M]
asum = sum(A)
rate = asum / 4 / M

for idx in AM:
    if idx < rate:
        print('No')
        break
else:
    print('Yes')
