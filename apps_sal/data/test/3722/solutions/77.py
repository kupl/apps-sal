import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2(): return list(map(int, sys.stdin.readline().rstrip()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())


N = I()
AA, AB, BA, BB = S(), S(), S(), S()
mod = 10**9 + 7

if N == 2:
    print((1))
    return

fib = [1, 1]
for i in range(N):
    fib.append((fib[-1] + fib[-2]) % mod)

if AB == 'A':
    if AA == 'A':
        print((1))
    else:
        if BA == 'B':
            print((pow(2, N - 3, mod)))
        else:
            print((fib[N - 2]))
else:
    if BB == 'B':
        print((1))
    else:
        if BA == 'A':
            print((pow(2, N - 3, mod)))
        else:
            print((fib[N - 2]))
