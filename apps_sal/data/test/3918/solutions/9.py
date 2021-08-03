n, k1, k2 = [int(x) for x in input().split()]
a = input().split()
b = input().split()
d = [abs(int(x) - int(y)) for x, y in zip(a, b)]
for i in range(k1 + k2):
    m = 0
    max_ind = 0
    for j in range(n):
        if d[j] >= m:
            m = d[j]
            max_ind = j
    d[max_ind] = abs(d[max_ind] - 1)
print(sum(x * x for x in d))
