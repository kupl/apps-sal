
import heapq


def solve_for_0(d, max_, ans):
    pos_M = list(d[max_])[0]
    pos_m = list(d[0])[0]

    for _ in range(max_):
        ans.append([pos_M, pos_m])


def solve_one_seg(d, max_, min_, ans):
    seg = list(d[max_])
    n = len(seg)

    if n <= 5:
        for _ in range(max_ - min_):
            ans.append(seg)
    else:
        ori = []
        for i in range(0, n, 2):
            if i == n - 1:
                ori[-1].append(seg[i])
            else:
                ori.append([seg[i], seg[i + 1]])

        for _ in range(max_ - min_):
            ans.extend(ori)


def push(d, x, val, i):
    if x not in d:
        d[x] = set()

    if val == 1:
        d[x].add(i)
    else:
        d[x].remove(i)

    if len(d[x]) == 0:
        del d[x]


def check(d):
    if len(d) != 2:
        return 'none', None

    max_ = max(list(d.keys()))
    min_ = min(list(d.keys()))

    if len(d[max_]) >= 2:
        return 'seg', [max_, min_]

    elif min_ == 0:
        return '0', [max_]

    return 'none', None


def pr(ans, n):
    print(len(ans))
    arr = [[0] * n for _ in range(len(ans))]

    for i, val in enumerate(ans):
        for ind in val:
            arr[i][ind] = 1
    S = ''
    for s in arr:
        S += ''.join([str(x) for x in s])
        S += '\n'
    print(S)


n = int(input())
arr = list(map(int, input().split()))
ans = []
Q = []
d = {}

for i, x in enumerate(arr):
    push(d, x, 1, i)
    heapq.heappush(Q, (-x, x, i))

if len(d) == 1:
    print(list(d.keys())[0])
    print(0)
else:
    while True:
        type_, arg = check(d)
        if type_ == 'none':
            val1, num1, i1 = heapq.heappop(Q)
            val2, num2, i2 = heapq.heappop(Q)
            push(d, num1, -1, i1)
            push(d, num2, -1, i2)
            ans.append([i1, i2])

            new1 = max(0, num1 - 1)
            new2 = max(0, num2 - 1)
            heapq.heappush(Q, (-new1, new1, i1))
            heapq.heappush(Q, (-new2, new2, i2))
            push(d, new1, 1, i1)
            push(d, new2, 1, i2)

        elif type_ == 'seg':
            max_, min_ = arg[0], arg[1]
            solve_one_seg(d, max_, min_, ans)

            print(min_)
            pr(ans, n)
            break
        else:
            max_ = arg[0]
            solve_for_0(d, max_, ans)

            print(0)
            pr(ans, n)
            break
