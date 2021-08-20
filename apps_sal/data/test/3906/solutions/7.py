M = 10 ** 9 + 7
array = [0] * 100010
array[0] = 1
array[1] = 1


def f(n):
    if array[n] == 0:
        array[n] = (f(n - 1) + f(n - 2)) % M
    return array[n]


for i in range(1, 100010):
    f(i)
(a, b) = map(int, input().split())
print((f(a) + f(b) - 1) * 2 % M)
