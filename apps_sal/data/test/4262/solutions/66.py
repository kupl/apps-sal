import itertools
n = int(input())
pl = list(map(int, input().split()))
ql = list(map(int, input().split()))
l = list(itertools.permutations(range(1, n + 1), n))
cnt = 1
(p, q) = (0, 0)
for i in l:
    if list(i) == pl:
        p = cnt
    if list(i) == ql:
        q = cnt
    cnt += 1
print(abs(p - q))
