n = int(input())
(d, x) = map(int, input().split())
data = [int(input()) for i in range(n)]
ans = n
for i in range(n):
    ans += (d - 1) // data[i]
print(ans + x)
