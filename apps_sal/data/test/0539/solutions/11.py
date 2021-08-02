n = int(input())

cnt = 0

for a in range(n + 1):
    for b in range(a, n + 1):
        c = a ^ b
        if c == 0 or c > n or a >= c or b >= c or a + b <= c:
            continue
        cnt += 1

print(cnt)
