n = int(input())
ans = 0
for i in range(1, n + 1):
    val = n // i
    ans += i * (val) * (val + 1) / 2
print(int(ans))
