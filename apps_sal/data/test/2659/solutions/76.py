from collections import deque
k = int(input())


def digsum(x): return sum(map(int, list(str(x))))
def dignorm(x): return x / digsum(x)


n = 1
order = 1
while k > 0:
    print(n)
    k -= 1
    if dignorm(n + 10**(order - 1)) > dignorm(n + 10**order):
        order += 1
    n += 10**(order - 1)
