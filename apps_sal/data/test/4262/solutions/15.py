import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

l = [i + 1 for i in range(N)]
for i, tpl in enumerate(itertools.permutations(l, N)):
    if tpl == P:
        a = i
    if tpl == Q:
        b = i
print(abs(a - b))
