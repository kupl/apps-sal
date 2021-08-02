s = input().split()

n, m = s
n = int(n)
m = int(m)
n *= 2
m *= 3
i = 1

while True:
    if n <= m:
        if i * 6 <= n:
            n += 2
        else:
            break
    else:
        if i * 6 <= m:
            m += 3
        else:
            break
    i += 1

print(max(n, m))
