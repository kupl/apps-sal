n = int(input())
a = [int(s) for s in input().split()]
ans = [0] * n
for i in range(n):
    ans[a[i] - 1] = i + 1
print(*ans)
