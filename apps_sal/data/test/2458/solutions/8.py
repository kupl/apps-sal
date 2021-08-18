import sys


def solve():
    MOD = 1000000007
    size = 100003
    t, groupsize = read()
    mem = [0] * size
    summ = [0] * size
    for i in range(len(mem)):
        mem[i] = ((mem[i - 1] + mem[i - groupsize] if i >= groupsize else mem[i - 1]) % MOD) if i > 0 else 1
    for i in range(len(summ)):
        summ[i] = (mem[i] + summ[i - 1]) % MOD if i > 0 else mem[i]
    res = list()
    for i in range(t):
        a, b = read()
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


def write(s="\n"):
    if s is None:
        s = ""
    if isinstance(s, list):
        s = "\n".join(map(str, s))
    if isinstance(s, tuple):
        s = " ".join(map(str, s))
    s = str(s)
    print(s, end="")


def run():
    if sys.hexversion == 50594544:
        sys.stdin = open("test.txt")
    res = solve()
    write(res)


run()
