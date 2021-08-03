MOD = 10**9 + 7
n = int(input())
a, b, c, d = [0 if input() == 'A' else 1 for _ in range(4)]
if (a, b, c, d) in ((0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 1), (1, 1, 0, 1), (1, 1, 1, 1)):
    print((1))
elif (a, b, c, d) in ((0, 1, 0, 0), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0)):
    if n == 2:
        print((1))
    else:
        print((pow(2, n - 3, MOD)))
else:
    a, b = 1, 1
    for i in range(n - 2):
        a, b = b, (a + b) % MOD
    print(a)
