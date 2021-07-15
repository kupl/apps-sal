from math import sqrt

n = int(input())
ans = float('inf')
for a in range(1, int(sqrt(n)) + 1):
    if n % a == 0:
        b = n // a
        ans = min(ans, max(len(str(a)), len(str(b))))
print(ans)
