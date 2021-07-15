import math

def is_prime(n):
    bound = int(math.sqrt(n + 1) + 1)
    for k in range(2, bound):
        if n % k == 0:
            return False
    return True


def solve():
    a, b = (int(x) for x in input().split())
    if a - b != 1:
        print('NO')
        return

    if is_prime(a+b):
        print('YES')
    else:
        print('NO')


num_tests = int(input())
for _ in range(num_tests):
    solve()

