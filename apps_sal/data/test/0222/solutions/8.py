import itertools


def try_sqrt(n):
    m = int(n ** 0.5)
    return True if abs(m * m - n) < 1e-06 else False


N = int(input())
if try_sqrt(N):
    print(0)
    quit()
L = list(str(N))
for i in reversed(range(1, len(L))):
    for num_l in itertools.combinations(L, i):
        if num_l[0] == '0':
            continue
        num = int(''.join(num_l))
        if try_sqrt(num):
            print(len(L) - i)
            quit()
print(-1)
