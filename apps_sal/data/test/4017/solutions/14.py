n = int(input())
A = list(map(int, input().split()))
s = sum(A)
s1 = s - max(A)
A = [(A[i], i + 1) for i in range(n)]
A.sort()
res = []
for i in range(n - 1):
    if s1 - A[i][0] == A[-1][0]:
        res.append(A[i][1])
if s1 - A[-2][0] == A[-2][0]:
    res.append(A[-1][1])
print(len(res))
for i in range(len(res)):
    print(res[i], end=' ')
