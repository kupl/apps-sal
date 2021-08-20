(n, m) = input().split()
(n, m) = (int(n), int(m))
i = 0
while True:
    if n > m:
        break
    n = n * 3
    m = m * 2
    i += 1
print(i)
