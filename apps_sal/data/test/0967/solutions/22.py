n = int(input())
a = list(map(int, input().split()))
ans = n - 1
for i in range(n - 1, 0, -1):
    if a[i - 1] > a[i]:
        break
    ans -= 1
print(ans)
