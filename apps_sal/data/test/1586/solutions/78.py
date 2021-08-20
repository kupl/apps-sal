n = int(input())
i = 10
ans = 0
while i <= n:
    ans += n // i
    i *= 5
print(ans if n & 1 == 0 else 0)
