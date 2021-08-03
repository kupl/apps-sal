n = int(input())

cnt = 0
for i in range(1, n + 1, 2):
    factors = 1
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            factors += 1
    if factors == 8:
        cnt += 1
print(cnt)
