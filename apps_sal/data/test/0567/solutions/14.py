n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    if min(l[i] - 1, 10 ** 6 - l[i]) > ans:
        ans = min(l[i] - 1, 10 ** 6 - l[i])
print(ans)
