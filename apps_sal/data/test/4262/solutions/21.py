import itertools
n = int(input())
p = [int(i) - 1 for i in input().split()]
q = [int(i) - 1 for i in input().split()]
m = sorted(p)
a = 0
b = 0
cnt = 1
for i in itertools.permutations(m, n):
    if list(i) == p:
        a += cnt
    if list(i) == q:
        b += cnt
    if a != 0 and b != 0:
        break
    else:
        cnt += 1

print(abs(a - b))
