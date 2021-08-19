import sys


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


N = ir()
answer = 0


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors[1:]


cand = make_divisors(N) + make_divisors(N - 1)
for x in cand:
    M = N
    while M % x == 0:
        M //= x
    r = M % x
    if r == 1:
        answer += 1
print(answer)
