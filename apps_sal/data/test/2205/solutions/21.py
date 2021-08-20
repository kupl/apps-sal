import sys
inf = float('inf')


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def input():
    return sys.stdin.readline().strip()


def running_xor(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0


n = int(input())
Arr = get_array()
ans = 0
for i in range(1, n):
    div = n // (i + 1)
    if div & 1:
        ans ^= running_xor(i)
    remainder = n % (i + 1)
    ans ^= running_xor(remainder)
for i in Arr:
    ans ^= i
print(ans)
