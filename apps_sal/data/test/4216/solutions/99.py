n = int(input())
ans = 10 ** 9
for i in range(1, int(n**0.5) + 1):
    if n % i != 0:
        continue
    ans = min(ans, max(len(str(i)), len(str(n // i))))
print(ans)
