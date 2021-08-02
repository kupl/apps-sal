import functools
import operator


mem = [0]
for i in range(1, 10 ** 6):

    mem.append(mem[-1] ^ i)

n = int(input())
ps = tuple(map(int, str.split(input())))
x = functools.reduce(operator.xor, ps)
for i in range(n):

    c, m = divmod(n, i + 1)
    if c & 1:

        x ^= mem[i]

    x ^= mem[m]

print(x)
