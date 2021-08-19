n = int(input())
A = list(map(int, input().split()))
ans = list(range(n))
for i in range(n):
    ans[A[i] - 1] = i + 1
print(' '.join(map(str, ans)))
