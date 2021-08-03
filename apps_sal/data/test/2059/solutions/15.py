n = int(input())
l1 = list(map(int, input().split()))
for i in range(0, n):
    if i == 0:
        ans = l1[i] // (n - 1)
    else:
        x = max(n - 1 - i, i)
        ans = min(ans, l1[i] // x)
print(ans)
