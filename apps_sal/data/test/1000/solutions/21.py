(n, v) = input().split()
n = int(n)
v = int(v)
if n <= v:
    print(n - 1)
else:
    summ = v
    for i in range(n - v - 1):
        summ += i + 2
    print(summ)
