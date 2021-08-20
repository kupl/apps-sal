N = int(input())
A = [int(x) for x in input().split()]


def count(n, Set):
    if not n in Set:
        Set.add(n)
        return 0
    else:
        return 1


Sieve = set()
extra = 0
for a in A:
    extra += count(a, Sieve)
print(N - extra if not extra & 1 else N - extra - 1)
