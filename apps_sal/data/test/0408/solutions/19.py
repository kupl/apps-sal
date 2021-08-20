(n, m) = list(map(int, input().split()))
i = 0
while n >= 2 and m >= 2:
    if m >= n:
        m -= 2
        n -= 1
    elif n > m:
        m -= 1
        n -= 2
    i += 1
if m == 1 and n >= 2:
    i += 1
if n == 1 and m >= 2:
    i += 1
print(i)
