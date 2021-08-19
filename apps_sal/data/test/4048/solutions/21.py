n = int(input())
for i in list(range(1, int(n ** 0.5) + 1))[::-1]:
    if n % i == 0:
        ans = i + n // i
        break
print(ans - 2)
