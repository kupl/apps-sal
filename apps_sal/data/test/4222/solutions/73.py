n, k = list(map(int, input().split()))
ans = [1] * n
for _ in range(k):
    d = int(input())
    li = list(map(int, input().split()))
    for i in li:
        ans[i - 1] = 0
print((sum(ans)))
