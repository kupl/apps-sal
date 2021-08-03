n = int(input())
ans = 0
for _ in range(n):
    l, r = map(int, input().split())
    ans += r - l
print(ans + n)
