n, m = list(map(int, input().split(" ")))
total = (n + m) / 3
cnt = 0
while cnt < total and n > 0 and m > 0:
    cnt += 1
    if n < m:
        n -= 1
        m -= 2
    else:
        n -= 2
        m -= 1

if n < 0 or m < 0: cnt -= 1
print(cnt)
