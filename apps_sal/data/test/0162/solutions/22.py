n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for item in a:
    if (k % item == 0):
        ans = max(ans, item)
print(k // ans)
