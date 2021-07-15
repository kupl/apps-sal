n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = x
for i in a:
    ans += (d-1) // i + 1
print(ans)
