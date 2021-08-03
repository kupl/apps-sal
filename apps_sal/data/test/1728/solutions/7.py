n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 1
for i in range(n - 1):
    if b[i + 1] != b[a[i] - 1]:
        ans += 1
print(ans)
