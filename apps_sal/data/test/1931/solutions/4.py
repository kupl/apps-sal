poss = [2]
i = 2
while poss[-1] <= 1000000000:
    poss.append(poss[-1] + 2 * i + i - 1)
    i += 1
for f in range(int(input())):
    n = int(input())
    m = 0
    i = 0
    while poss[i + 1] <= n:
        i += 1
    n -= poss[i]
    if n >= 0:
        m += 1
    while n > 1:
        while poss[i] > n:
            i -= 1
        n -= poss[i]
        m += 1
    print(m)
