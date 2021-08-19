from operator import itemgetter
(n, m) = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
d_dict = dict()
for i in range(m):
    d_dict[i + 1] = []
for i in range(n):
    if d[i]:
        d_dict[d[i]].append(i)


def check_feasibility(x):
    tmp_d = d[:x]
    set_tmd_d = set(tmp_d) - set([0])
    if len(set_tmd_d) < m:
        return False
    else:
        index_list = [[[j for j in d_dict[i + 1] if j < x][-1], a[i]] for i in range(m)]
        index_list = sorted(index_list, key=itemgetter(0))
        tmp = 0
        for i in range(m):
            tmp += index_list[i][1]
            if tmp + i > index_list[i][0]:
                return False
    return True


if check_feasibility(n):
    right = n
    left = 1
    mid = (left + right) // 2
    cur_value = check_feasibility(mid)
    while left != right:
        if not cur_value:
            left = mid + 1
        else:
            right = mid
        mid = (left + right) // 2
        cur_value = check_feasibility(mid)
    print(mid)
else:
    print(-1)
