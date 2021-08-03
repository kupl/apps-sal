n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0

for i in range(n):
    ans += b[i]
for j in range(n - 1):
    if a[j] == a[j + 1] - 1:
        ans += c[(a[j] - 1)]

print(ans)
