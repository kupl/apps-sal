N = int(input())

g = 0
for n in range(1, N + 1):
    if n % 2 == 0:
        g += 1

ANS = (N - g) / N

print(ANS)
