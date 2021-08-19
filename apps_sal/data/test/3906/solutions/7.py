M = 10 ** 9 + 7  # MODULO
array = [0] * 100010  # Extra because im bad
array[0] = 1
array[1] = 1
# array[2] = 2


def f(n):
    if array[n] == 0:
        array[n] = (f(n - 1) + f(n - 2)) % M
    return array[n]


# To initialize, don't use sys.setrecursionlimit(99999). It's bad.
for i in range(1, 100010):
    f(i)  # Calculates the value but doesn't do anything with it
# Now you can do
# a, b = tuple(map(int, input().split()))
a, b = map(int, input().split())  # No need tuple, python is smart :)
print(((f(a) + f(b) - 1) * 2) % M)
