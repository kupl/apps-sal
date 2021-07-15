import itertools
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

n = [i+1 for i in range(N)]

a = 0
b = 0
i = 0
for x in itertools.permutations(n):
    if list(x) == P:
        a = i
    if list(x) == Q:
        b = i
    i += 1

print(abs(a - b))
