N = int(input())

A, B = [], []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

A.sort()
B.sort()

cnt = 0
if(N % 2 == 1):
    l = A[N // 2]
    r = B[N // 2]
    cnt = r - l + 1
else:
    l = A[N // 2 - 1] + A[N // 2]
    r = B[N // 2 - 1] + B[N // 2]
    cnt = r - l + 1
print(cnt)
