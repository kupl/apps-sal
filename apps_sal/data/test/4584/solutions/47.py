n = int(input())
ans = [0] * n
l = list(map(int, input().split()))
for i in range(n - 1):
    ans[l[i] - 1] += 1
for i in range(n):
    print(ans[i])
