n, m = [int(i) for i in input().split()]
lst = [0 for i in range(m)]
inp = [int(i) for i in input().split()]

for i in inp:
    lst[i - 1] += 1
lst = [i * (i - 1) // 2 for i in lst if i > 1]
print((n * (n - 1) // 2) - sum(lst))
