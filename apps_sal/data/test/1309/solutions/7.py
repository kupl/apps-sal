n = int(input())
a = list(map(int, input().split()))
a.sort()
an = 10 ** 9

for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        if i == j:
            continue
        b = a[:]
        del b[j], b[i]
        c = 0
        for k in range(0, 2 * n - 2, 2):
            c += abs(b[k] - b[k + 1])
        an = min(an, c)
        #print(an, b)
print(an)

