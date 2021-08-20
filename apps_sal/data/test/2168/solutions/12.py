n = int(input())
M = []
A = []
for i in range(n):
    a = list(map(int, input().split(' ')))
    M.append(a[0])
    A.append(max(a[1:]))
temp = max(A)
ans = 0
for i in range(n):
    ans += abs(temp - A[i]) * M[i]
print(ans)
