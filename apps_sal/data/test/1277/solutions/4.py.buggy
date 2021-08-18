import sys
sys.setrecursionlimit(10 ** 9)

n, u, v = list(map(int, input().split()))
u -= 1
v -= 1
ab = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)


def dfs1(pos, before_pos):
    for next_pos in ab[pos]:
        if next_pos == before_pos:
            continue
        if next_pos == u:
            return True, [pos]
        tf, root = dfs1(next_pos, pos)
        if tf:
            root.append(pos)
            return True, root
    return False, []


root = dfs1(v, -1)[1]
root = root[::-1]
root.append(u)
n = (len(root) + 1) // 2
pos = root[n]
before_pos = root[n - 1]

max_len = n


def dfs2(pos, before_pos, cnt):
    nonlocal max_len
    cnt += 1
    max_len = max(max_len, cnt)
    if cnt < n - 1:
        dfs2(root[cnt + 1], pos, cnt)
    else:
        for next_pos in ab[pos]:
            if next_pos == before_pos:
                continue
            dfs2(next_pos, pos, cnt)


dfs2(pos, before_pos, n - 1)
ans = max_len - 1
ans = max(ans, 0)
print(ans)
