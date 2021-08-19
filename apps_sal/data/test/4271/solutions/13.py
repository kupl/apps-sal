n = int(input())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
c = [int(s) for s in input().split()]
ans = b[a[0] - 1]
for i in range(1, n):
    ans += b[a[i] - 1]
    if a[i] == a[i - 1] + 1:
        ans += c[a[i] - 2]
print(ans)
