import sys
sys.setrecursionlimit(15000000)


def solve():
    n = int(input())
    mem = [1000000] * (n + 1)
    mem[0] = 0
    for i in range(1, n + 1):
        ncopy = i
        while ncopy > 0:
            last = ncopy % 10
            ncopy //= 10
            if last != 0 and i - last >= 0:
                mem[i] = min(mem[i], 1 + mem[i - last])
    print(mem[n])


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
solve()
