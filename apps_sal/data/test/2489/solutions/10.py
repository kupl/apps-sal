N = int(input())
A = [int(x) for x in input().split()]
M = max(A)
count = [0] * (M + 1)
for i in range(N):
    count[A[i]] += 1
check = [True] * (M + 1)
for a in range(1, M + 1):
    if count[a] > 0 and check[a] == True:
        for k in range(2, M // a + 1):
            check[a * k] = False
ans = 0
for i in range(N):
    if count[A[i]] == 1 and check[A[i]] == True:
        ans += 1
print(ans)
