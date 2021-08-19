from sys import stdin, stdout
import itertools
(n, m) = list(map(int, stdin.readline().split()))
friends = [0] * 512
exists = [0] * 512
costs_min = [0] * 512
costs_2 = [0] * 512
index_min = [0] * 512
index_2 = [0] * 512
count_friends = [0] * 512


def top_to_idx(top):
    ans = 0
    for t in top:
        ans += 1 << t - 1
    return ans


def idx_to_top(idx):
    ans = []
    for i in range(9):
        if idx & 1 << i:
            ans.append(i + 1)
    return ans


for i in range(n):
    top = list(map(int, stdin.readline().split()))[1:]
    friends[top_to_idx(top)] += 1


def subset(i, j):
    for s in range(9):
        if i & 1 << s and (not j & 1 << s):
            return False
    return True


for i in range(512):
    for j in range(512):
        if subset(j, i):
            count_friends[i] += friends[j]
for i in range(m):
    pizza = list(map(int, stdin.readline().split()))
    top_idx = top_to_idx(pizza[2:])
    cost = pizza[0]
    exists[top_idx] = True
    if costs_min[top_idx] == 0 or cost < costs_min[top_idx]:
        costs_2[top_idx] = costs_min[top_idx]
        index_2[top_idx] = index_min[top_idx]
        costs_min[top_idx] = cost
        index_min[top_idx] = i + 1
    elif costs_2[top_idx] == 0 or cost < costs_2[top_idx]:
        costs_2[top_idx] = cost
        index_2[top_idx] = i + 1
best_matches = -1
best_cost = -1
best = None
for p1 in range(512):
    for p2 in range(p1, 512):
        if not exists[p1] or not exists[p2]:
            continue
        if p1 == p2 and index_2[p1] == 0:
            continue
        p = p1 | p2
        matches = count_friends[p]
        cost = costs_min[p1] + costs_min[p2] if p1 != p2 else costs_min[p1] + costs_2[p2]
        if best_matches == -1 or matches > best_matches or (matches == best_matches and cost < best_cost):
            best = (index_min[p1], index_min[p2]) if p1 != p2 else (index_min[p1], index_2[p2])
            best_matches = matches
            best_cost = cost
print(best[0], best[1])
