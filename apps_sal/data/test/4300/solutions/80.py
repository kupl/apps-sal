n = int(input())
lis = list(map(int, input().split()))
ans = 0


for i in range(0, n - 1):
    for t in range(i + 1, n):
        con = lis[i] * lis[t]
        ans += con


print(ans)
