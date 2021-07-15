n, x = list(map(int, input().split()))
cur = x
sad = 0
for i in range(n):
    c, m = input().split()
    m = int(m)
    if c == '+':
        cur += m
    else:
        if cur >= m:
            cur -= m
        else:
            sad += 1
print(cur, sad)

