from itertools import permutations

N = int(input())

P = input()
Q = input()

a = 0
b = 0
for i, p in enumerate(permutations(list(range(1, N + 1))), 1):
    s = ' '.join([str(v) for v in p])
    if s == P:
        a = i
    if s == Q:
        b = i

    if a and b:
        print((abs(a - b)))
        return
