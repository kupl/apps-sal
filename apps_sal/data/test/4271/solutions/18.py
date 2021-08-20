n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(0, n):
    ans += b[a[i] - 1]
    if i >= 1:
        if a[i] == a[i - 1] + 1:
            ans += c[a[i] - 2]
print(ans)
