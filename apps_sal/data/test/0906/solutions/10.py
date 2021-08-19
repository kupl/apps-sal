inp = input()
(n, m, k) = map(int, inp.split())
if n % 2 != m % 2 and k == -1:
    print(0)
else:
    ret = pow(2, (n - 1) * (m - 1), 10 ** 9 + 7)
    print(ret)
