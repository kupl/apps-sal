n, m = map(int, input().split())
a = m // n
di = []
for i in range(1, min(a + 1, int(m**0.5) + 1)):
    if m % i == 0:
        di.append(i)
        if i != m // i and a >= m // i:
            di.append(m // i)
di.sort()
print(di[-1])
