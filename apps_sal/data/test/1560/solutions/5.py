n = int(input())
s = str(input())
r = b = 0
m = 0
m2 = 0
for i in range(n):
    if s[i] == 'r':
        r += 1
    else:
        b += 1
if n % 2:
    if r > b:
        for i in range(n):
            if s[i] == 'b' and i % 2 == 0:
                m += 1
        for i in range(n):
            if s[i] == 'b' and i % 2:
                m2 += 1
        print(min(m + (n - 1) // 2 - b, m2 + (n + 1) // 2 - b))
    else:
        for i in range(n):
            if s[i] == 'r' and i % 2 == 0:
                m += 1
        for i in range(n):
            if s[i] == 'r' and i % 2:
                m2 += 1
        print(min(m + (n - 1) // 2 - r, m2 + (n + 1) // 2 - r))
elif r > b:
    for i in range(n):
        if s[i] == 'b' and i % 2 == 0:
            m += 1
    for i in range(n):
        if s[i] == 'b' and i % 2:
            m2 += 1
    print(min(m, m2) + n // 2 - b)
else:
    for i in range(n):
        if s[i] == 'r' and i % 2 == 0:
            m += 1
    for i in range(n):
        if s[i] == 'r' and i % 2:
            m2 += 1
    print(min(m, m2) + n // 2 - r)
