(n, k) = map(int, input().split())
ls = list(map(int, input().split()))
res = {}
avail = {}
left = {}
right = {}
left[0] = -1
for i in range(1, n):
    left[i] = i - 1
right[n - 1] = -1
for i in range(n - 1):
    right[i] = i + 1
for i in range(n):
    avail[i] = True
ls = [(ls[i], i) for i in range(n)]
ls.sort(key=lambda x: x[0])
ls.reverse()
turn = 1
for i in range(n):
    if avail[ls[i][1]] == True:
        avail[ls[i][1]] = False
        cur = ls[i][1]
        res[cur] = turn
        if left[cur] != -1:
            right[left[cur]] = right[cur]
        if right[cur] != -1:
            left[right[cur]] = left[cur]
        for _ in range(k):
            cur = right[cur]
            if cur == -1:
                break
            avail[cur] = False
            res[cur] = turn
            if left[cur] != -1:
                right[left[cur]] = right[cur]
            if right[cur] != -1:
                left[right[cur]] = left[cur]
        cur = ls[i][1]
        for _ in range(k):
            cur = left[cur]
            if cur == -1:
                break
            avail[cur] = False
            res[cur] = turn
            if left[cur] != -1:
                right[left[cur]] = right[cur]
            if right[cur] != -1:
                left[right[cur]] = left[cur]
        if turn == 1:
            turn = 2
        else:
            turn = 1
for i in range(n):
    print(res[i], end='')
