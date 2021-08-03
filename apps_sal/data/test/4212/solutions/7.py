from itertools import combinations_with_replacement

n, m, q = map(int, input().split())
conditions = []
for i in range(q):
    conditions.append(list(map(int, input().split())))

cands = []
for i in combinations_with_replacement(list(range(1, m + 1)), n):
    cands.append(i)

maxi = 0
for cand in cands:
    score = 0
    for condition in conditions:
        if cand[condition[1] - 1] - cand[condition[0] - 1] == condition[2]:
            score += condition[3]
    if score > maxi:
        maxi = score
print(maxi)
