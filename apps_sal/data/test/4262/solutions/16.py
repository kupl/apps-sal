import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pattern = list(itertools.permutations(list(range(1, n + 1))))


a = 0
b = 0

for x in pattern:
    new_x = list(x)
    if new_x == p:
        a = pattern.index(x)
    if new_x == q:
        b = pattern.index(x)


print((abs(a - b)))
