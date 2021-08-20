n = int(input())
a = list(map(int, input().split()))
(b, idx) = list(zip(*sorted(zip(a, list(range(1, n + 1))))))
if b[-1] < 0:
    print(n - 1)
    for i in range(n - 1):
        print((n - i, n - i - 1))
elif b[0] >= 0:
    print(n - 1)
    for i in range(n - 1):
        print((i + 1, i + 2))
else:
    print(2 * n - 2)
    if b[-1] > abs(b[0]):
        for i in range(n):
            if i + 1 != idx[-1]:
                print((idx[-1], i + 1))
        for i in range(n - 1):
            print((i + 1, i + 2))
    else:
        for i in range(n):
            if i + 1 != idx[0]:
                print((idx[0], i + 1))
        for i in range(n - 1):
            print((n - i, n - i - 1))
