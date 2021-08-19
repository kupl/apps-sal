from collections import defaultdict
T = int(input())
for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]
    els = sorted(set(A))
    pos = defaultdict(list)
    for (i, el) in enumerate(A):
        pos[el].append(i)
    DMAX = {}
    for el in list(pos.keys()):
        dmax = -1
        arr = [-1] + sorted(pos[el]) + [N]
        for i in range(1, len(arr)):
            dmax = max(dmax, arr[i] - arr[i - 1])
        DMAX[el] = dmax
    ci = 0
    answer = []
    for i in range(N - 1, -1, -1):
        while ci < len(els) and DMAX[els[ci]] > i + 1:
            ci += 1
        if ci >= len(els):
            answer.append(-1)
        else:
            answer.append(els[ci])
    print(' '.join(map(str, answer[::-1])))
