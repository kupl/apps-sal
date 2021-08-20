import itertools
import collections
N = int(input())
Ls = list(map(int, input().split()))
L_combination = itertools.combinations(Ls, 3)
ans = 0
for sanpenList in L_combination:
    checker = set(sanpenList)
    if len(sanpenList) != len(checker):
        continue
    if max(sanpenList) * 2 >= sum(sanpenList):
        continue
    ans += 1
print(ans)
