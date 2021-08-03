n, t = map(int, input().split())
lis = list(map(int, input().split()))

ans = t
for i in range(1, n):
    if lis[i] - lis[i - 1] >= t:
        ans += t
    else:
        ans += lis[i] - lis[i - 1]

print(ans)
