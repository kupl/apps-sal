n = int(input())
A = list(map(int, input().split()))
for i in range(n - 1):
    A[i] = A[i] - 1
res = [[] for i in range(n)]

for i in range(n - 1):
    res[A[i]].append(i)

for i in range(n):
    print(len(res[i]))
