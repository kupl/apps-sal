n = int(input())
s = []
i = 1
while i * i <= n:
    if n % i == 0:
        y = n // i
        a = i
        x = (a * y * (y + 1)) // 2 - (a - 1) * y
        s.append(x)
        j = n // i
        if j > i:
            y = n // j
            a = j
            x = (a * y * (y + 1)) // 2 - (a - 1) * y
            s.append(x)
    i += 1
s = set(s)
s = list(s)
s.sort()
print(*s)

