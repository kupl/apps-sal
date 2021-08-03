def prime_factor_table(n):
    table = [0] * (n + 1)

    for i in range(2, n + 1):
        if table[i] == 0:
            for j in range(i + i, n + 1, i):
                table[j] = i

    return table


l = prime_factor_table(100000)
l[0] = 1
l[1] = 1
l2 = [0] * 100000

for i in range(1, 100000, 2):
    x = (i + 1) // 2
    if l[i] == 0 and l[x] == 0:
        l2[i] = 1

l3 = [0]
for i in range(100000):
    x = l3[i] + l2[i]
    l3.append(x)

Q = int(input())
for i in range(Q):
    a, b = list(map(int, input().split()))
    print((l3[b + 1] - l3[a]))
