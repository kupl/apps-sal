n = int(input())


def k(x):
    twos = 0
    while x % 2 == 0:
        x //= 2
        twos += 1
    threes = 0
    while x % 3 == 0:
        x //= 3
        threes += 1
    return (twos, -threes)


A = sorted(map(int, input().split()), key=k)
print(' '.join(map(str, A)))
