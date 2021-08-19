import math
s = int(input())
maxn = s // 3
ans = 0
for i in range(1, maxn + 1):
    b = s - 3 * i
    ans += math.factorial(b + i - 1) // (math.factorial(b) * math.factorial(i - 1))
print(ans % (10 ** 9 + 7))
