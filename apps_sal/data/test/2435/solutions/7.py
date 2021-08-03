from queue import Queue
for _ in range(int(input())):
    n, x, m = list(map(int, input().split()))

    ans = [x, x]
    for i in range(m):
        l, r = list(map(int, input().split()))
        if ans[1] < l or ans[0] > r:
            continue
        else:
            ans[0] = min(ans[0], l)
            ans[1] = max(ans[1], r)
    print(ans[1] - ans[0] + 1)
