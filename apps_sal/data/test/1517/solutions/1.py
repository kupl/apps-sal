import math
ans = [1, 3, 15, 133, 2025, 37851, 1030367, 36362925]
n = int(input())
if n % 2 == 1:
    print(ans[n // 2] * math.factorial(n) % 1000000007)
else:
    print(0)
