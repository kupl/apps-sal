n = int(input())
t = [0] * (n + 1)
for j in range(2, n + 1):
    y = j
    for i in range(2, n + 1):
        while y % i == 0:
            t[i] += 1
            y = y // i
ans = 1
p = 10 ** 9 + 7
for i in t:
    if i != 0:
        ans *= i + 1
        ans %= p
print(ans)
