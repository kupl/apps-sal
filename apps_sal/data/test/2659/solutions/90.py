from collections import deque
k = int(input())

digsum = lambda x: sum(list(map(int, list(str(x)))))
dignorm = lambda x: x / digsum(x)

n = 1
order = 1
while k > 0:
    print(n)
    k -= 1
    if dignorm(n + 10**(order - 1)) > dignorm(n + 10**order):
        order += 1
    n += 10**(order - 1)
