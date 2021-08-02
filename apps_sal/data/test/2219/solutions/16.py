t = int(input())


def solve(n, k):
    acc = 0
    while n > 0:
        if n % k == 0:
            acc += 1
            n //= k
        else:
            acc += n % k
            n -= n % k
    return acc


for query in range(t):
    n, k = list(map(int, input().strip().split()))
    print(solve(n, k))
