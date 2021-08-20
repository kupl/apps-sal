n = int(input())
ans = float('inf')
for i in range(1, int(n ** 0.5) + 2):
    if n % i == 0:
        j = n // i
        res = max(len(str(i)), len(str(j)))
        ans = min(ans, res)
print(ans)
