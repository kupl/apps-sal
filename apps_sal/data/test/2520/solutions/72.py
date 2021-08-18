from collections import Counter

N, M, K = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

friend_g = [set() for i in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    friend_g[a].add(b)
    friend_g[b].add(a)
friend_count = [len(s) for s in friend_g]

g_nums = [-1] * N
current_g_num = 0
for i in range(N):
    if g_nums[i] == -1:
        g_nums[i] = current_g_num
        q = [i]
        while q:
            t = q.pop()
            for friend in friend_g[t]:
                if g_nums[friend] == -1:
                    g_nums[friend] = current_g_num
                    q.append(friend)
        current_g_num += 1

block_count = [0] * N
for c, d in CD:
    c, d = c - 1, d - 1
    if g_nums[c] == g_nums[d]:
        block_count[c] += 1
        block_count[d] += 1

g_nums_counter = Counter(g_nums)
print((*(g_nums_counter[g_nums[i]] - friend_count[i] - block_count[i] - 1 for i in range(N))))
