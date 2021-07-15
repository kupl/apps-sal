import itertools
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
S = [i for i in range(1, N+1)]

perm = list(itertools.permutations(S))
ans = []
for i, p in enumerate(perm):
    if list(p) == P or list(p) == Q:
        ans.append(i+1)

if len(ans) > 1:
    print(abs(ans[0] - ans[1]))
else:
    print(0)
