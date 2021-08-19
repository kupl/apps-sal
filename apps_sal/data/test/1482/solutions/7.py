(n, k) = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
s = set(range(1, n * k + 1))
for ai in a:
    s.remove(ai)
for ai in a:
    print(ai, end='')
    for i in range(n - 1):
        print(' ' + str(s.pop()), end='')
    print()
