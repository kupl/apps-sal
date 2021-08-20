(x, y) = list(map(int, input().split()))
n = x - y
j = n
c = 0
if j < 0:
    print(c)
elif j == 0:
    print('infinity')
else:
    result_set = set()
    sqrtn = int(n ** 0.5)
    for i in range(1, sqrtn + 1):
        (q, r) = (n / i, n % i)
        if r == 0:
            if q > y:
                result_set.add(q)
            if i > y:
                result_set.add(i)
    print(len(result_set))
