mod = 10 ** 9
FibArray = [1, 1]


def fibonacci(n):
    if n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a[query[1] - 1] = query[2]
    elif query[0] == 3:
        d = query[3]
        for i in range(query[1] - 1, query[2]):
            a[i] += d
    else:
        (l, r) = (query[1], query[2])
        s = 0
        for x in range(r - l + 1):
            s += fibonacci(x + 1) * a[l + x - 1]
        print(s % mod)
