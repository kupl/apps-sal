n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = x
for i in range(n):
    ans += ((d + a[i] - 1) // a[i])
print(ans)
