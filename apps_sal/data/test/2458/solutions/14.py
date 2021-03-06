import sys
import array


def solve():
    MOD = 1000000007
    size = 100003
    (t, groupsize) = read()
    mem = array.array('i', (0 for i in range(0, size)))
    summ = array.array('i', (0 for i in range(0, size)))
    mem[0] = 1
    for i in range(1, groupsize):
        mem[i] = mem[i - 1] % MOD
    for i in range(groupsize, len(mem)):
        mem[i] = (mem[i - 1] + mem[i - groupsize]) % MOD
    summ[0] = mem[0]
    for i in range(1, len(summ)):
        summ[i] = (mem[i] + summ[i - 1]) % MOD
    res = list()
    for i in range(t):
        (a, b) = read()
        res.append((summ[b] - summ[a - 1] + MOD) % MOD)
    return res


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs
    if mode == 1:
        return inputs.split()
    if mode == 2:
        return list(map(int, inputs.split()))


def write(s='\n'):
    if s is None:
        s = ''
    if isinstance(s, list):
        s = '\n'.join(map(str, s))
    if isinstance(s, tuple):
        s = ' '.join(map(str, s))
    s = str(s)
    print(s, end='')


def run():
    res = solve()
    write(res)


run()
