from itertools import permutations
n = int(input())
p = tuple(map(int, input().split(' ')))
q = tuple(map(int, input().split(' ')))
x = [i for i in range(1, n + 1)]
ls = list(permutations(x))
i = 0
for per in ls:
    if per == p:
        a = i
    if per == q:
        b = i
    i += 1
print(abs(a - b))
