n = int(input())
s = list(input())
x = list(map(int, input().split()))

ans = 10**10

for i in range(n - 1):
    if s[i] == "R" and s[i + 1] == "L":
        ans = min(ans, (x[i + 1] - x[i]) // 2)

if ans > 10 ** 9:
    ans = -1

print(ans)
