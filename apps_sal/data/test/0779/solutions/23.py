# This code sucks, you know it and I know it.
# Move on and call me an idiot later.

n = int(input())
cnt = 0
for i in range(1, (n // 2) + 1):
    if (n - i) % i == 0:
        cnt += 1
print(cnt)
