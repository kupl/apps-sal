from heapq import heappush, heapreplace
(n, k, q) = list(map(int, input().split()))
a = list(map(int, input().split()))
window = []
window_set = set()
min_pr = 10 ** 10
min_pr_id = 0
for i in range(q):
    (type, id) = list(map(int, input().split()))
    if type == 1:
        if len(window) < k:
            heappush(window, (a[id - 1], id))
            min_pr = min(min_pr, a[id - 1])
        elif a[id - 1] > min_pr:
            heapreplace(window, (a[id - 1], id))
            min_pr = window[0][0]
    elif id in [i[1] for i in window]:
        print('YES')
    else:
        print('NO')
