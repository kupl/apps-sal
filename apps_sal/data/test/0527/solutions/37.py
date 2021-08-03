from bisect import bisect_left


def solve():
    S = input()
    T = input()
    if not set(T) <= set(S):
        return -1

    pos = {c: [] for c in "abcdefghijklmnopqrstuvwxyz"}
    for i, c in enumerate(S):
        pos[c].append(i)
    ans = 0
    cur_pos = 0
    for t in T:
        nxt_idx = bisect_left(pos[t], cur_pos)
        if nxt_idx == len(pos[t]):
            ans += len(S)
            cur_pos = 0
            nxt_idx = bisect_left(pos[t], cur_pos)
            cur_pos = pos[t][nxt_idx] + 1
        else:
            cur_pos = pos[t][nxt_idx] + 1

    return ans + cur_pos


print((solve()))
