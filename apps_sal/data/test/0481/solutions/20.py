n, x = [int(i) for i in input().split(' ')]

cnt = 0

for i in range(1, n + 1):
    if (x % i == 0):
        if (x // i <= n):
            cnt += 1

print(cnt)

