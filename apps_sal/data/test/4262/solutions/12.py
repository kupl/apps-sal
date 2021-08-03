import itertools
n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

l = [i for i in range(1, n + 1)]
p = itertools.permutations(l, n)
i = 0

for v in itertools.permutations(l, n):
    i += 1
    if(v == P):
        a = i
    if(v == Q):
        b = i
print(abs(a - b))
