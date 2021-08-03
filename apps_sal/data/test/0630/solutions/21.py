# python3
# utf-8

def solve():
    n, k = (int(x) for x in input().split())
    idx___parent = [int(x) - 1 for x in input().split()]
    idx___l_cl = [max(0, idx - k) for idx in range(n)]
    idx___r_op = [min(n, idx + k + 1) for idx in range(n)]

    idx___message_count = []
    for idx in range(n):
        curr_l_cl = idx___l_cl[idx]
        curr_r_op = idx___r_op[idx]
        if idx___parent[idx] == -1:
            idx___message_count.append(curr_r_op - curr_l_cl)
            continue
        parent = idx___parent[idx]
        prev_r_op = idx___r_op[parent]
        curr_message_count = idx___message_count[parent]
        if prev_r_op > curr_l_cl:
            curr_l_cl = prev_r_op
        curr_message_count += curr_r_op - curr_l_cl
        idx___message_count.append(curr_message_count)
    print(*idx___message_count)


t = 1
# t = int(input())
for _ in range(t):
    solve()
