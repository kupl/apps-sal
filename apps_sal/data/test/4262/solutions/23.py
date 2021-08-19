import itertools
N = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
l = list(itertools.permutations(range(1, N + 1)))
a = 0
b = 0
for i in range(len(l)):
    s = [i for i in l[i]]
    if s == p:
        a = i
    if s == q:
        b = i
print(abs(a - b))
