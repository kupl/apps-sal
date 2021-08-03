import sys
import array
import io


def solve():
    MOD = 1000000007
    size = 100003
    t, groupsize = read()
    mem = array.array('i', (0 for i in range(0, size)))
    summ = array.array('i', (0 for i in range(0, size)))
    mem[0] = 1
    for i in range(1, groupsize):
        mem[i] = (mem[i - 1]) % MOD
    for i in range(groupsize, len(mem)):
        mem[i] = (mem[i - 1] + mem[i - groupsize]) % MOD
    summ[0] = mem[0]
    for i in range(1, len(summ)):
        summ[i] = (mem[i] + summ[i - 1]) % MOD
    # res = list()
    output = io.StringIO()
    for i in range(t):
        a, b = read()
        strtemp = str((summ[b] - summ[a - 1] + MOD) % MOD)
        output.write(strtemp + '\n')
        # res.append((summ[b]-summ[a-1]+MOD)%MOD)
    print(output.getvalue())


def read(mode=2):
    inputs = input().strip()
    if mode == 0:
        return inputs  # String
    if mode == 1:
        return inputs.split()  # List of strings
    if mode == 2:
        return list(map(int, inputs.split()))  # List of integers


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
