n = int(input())
val = 0
ans = float('inf')
for i in range(1, int(n ** 0.5 + 1)):
    if n % i == 0:
        val = max(len(str(i)), len(str(int(n / i))))
        ans = min(ans, val)
print(ans)
