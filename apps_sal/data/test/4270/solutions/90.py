n = int(input())
A = sorted(list(map(int, input().split())))
ans = A[0]
for i in range(n - 1):
    ans = (ans + A[i + 1]) / 2
print(ans)
