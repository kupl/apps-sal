n = int(input())
ans = float('inf')
for i in range(1, int(n**.5) + 1):
    if i * (n // i) == n:
        ans = min(ans, abs(i + (n // i)) - 2)
print(ans)
