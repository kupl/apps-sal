n = int(input())
A = list(map(int, input().split()))
total = sum(A) ** 2
for i in range(n):
    total -= A[i] ** 2
ans = total // 2 % (10 ** 9 + 7)
print(ans)
