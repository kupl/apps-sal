import time
MM = 1000000007


def func(a, b, k):
    if b == 0:
        return divmod(10 ** k - 1, a)[0] - divmod(10 ** (k - 1) - 1, a)[0]
    else:
        return divmod(10 ** k - 1, a)[0] - divmod((b + 1) * 10 ** (k - 1) - 1, a)[0] + divmod(b * 10 ** (k - 1) - 1, a)[0] + 1


(n, k) = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
start = time.time()
s = 1
for i in range(divmod(n, k)[0]):
    s *= func(a[i], b[i], k)
    s = divmod(s, MM)[1]
print(s)
finish = time.time()
