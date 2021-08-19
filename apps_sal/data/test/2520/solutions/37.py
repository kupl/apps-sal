from collections import Counter
(n, m, k) = list(map(int, input().split()))
f_adj_list = [[] for i in range(n)]
b_adj_list = [[] for i in range(n)]
for i in range(m):
    (_, __) = list(map(int, input().split()))
    _ -= 1
    __ -= 1
    f_adj_list[_].append(__)
    f_adj_list[__].append(_)
for j in range(k):
    (_, __) = list(map(int, input().split()))
    _ -= 1
    __ -= 1
    b_adj_list[_].append(__)
    b_adj_list[__].append(_)
group_id = [None for i in range(n)]
for i in range(n):
    if group_id[i] is not None:
        continue
    newly_visited = [i]
    group_id[i] = i
    while len(newly_visited) > 0:
        now = newly_visited.pop()
        for j in f_adj_list[now]:
            if group_id[j] is not None:
                continue
            newly_visited.append(j)
            group_id[j] = i
cnt = Counter(group_id)
ans_list = []
for i in range(n):
    ans = cnt[group_id[i]]
    ans -= 1
    ans -= len(f_adj_list[i])
    for j in b_adj_list[i]:
        if group_id[i] == group_id[j]:
            ans -= 1
    ans_list.append(ans)
print(' '.join(map(str, ans_list)))
