[n, m] = [int(i) for i in input().split()]
cnt = 0
while n < m:
    if m % 2:
        m += 1
        cnt += 1
    else:
        m //= 2
        cnt += 1
print(cnt + n - m)
