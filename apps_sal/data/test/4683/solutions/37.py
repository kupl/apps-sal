n = int(input())
a = list(map(int, input().split()))
count = 0
ans = 0
for i in range(1, n):
    count += a[-i]
    ans += a[-i - 1] * count
    ans = ans % (10**9 + 7)
print(ans)
