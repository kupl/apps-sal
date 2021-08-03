def maxseg(a):
    cur_max = 0
    global_max = 0
    pre_ = 0

    for i, x in enumerate(a):
        if x > 0:
            cur_max = max(x, cur_max + pre_ + x)
            global_max = max(global_max, cur_max)
        else:
            pre_ = x

    return global_max


def push(d, u, i):
    if u not in d:
        d[u] = []
    d[u].append(i)


def get_sum(a, l, r):
    if l == 0:
        return a[r]
    return a[r] - a[l - 1]


def get_array(a, pre_sum):
    cur = 0
    arr = []

    for i, x in enumerate(a):
        s = 0
        if i > 0:
            s += get_sum(pre_sum, a[i - 1], a[i])

        if i == 0 or s == 0:
            cur += 1
        else:
            arr.append(cur)
            arr.append(-s)
            cur = 1

    arr.append(cur)
    return arr


n, c = map(int, input().split())
a = list(map(int, input().split()))

d = {}
pre_sum = [0] * len(a)
pre = 0

for i, x in enumerate(a):
    if x == c:
        pre += 1
    else:
        push(d, x, i)
    pre_sum[i] = pre

max_ = 0
for pos_arr in d.values():
    arr = get_array(pos_arr, pre_sum)
    max_ = max(max_, maxseg(arr))

print(max_ + pre_sum[-1])
