n = int(input())
ans = 10000000000000

for i in range(1, int(n**0.5) + 1):
    if n % i != 0:
        continue

    j = n // i
    ans = min(ans, (i - 1) + (j - 1))

print(ans)
