t = int(input())
for z in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ret = [0 for i in range(n)]
    was = set()
    can = set([i for i in range(1, n + 1)])
    for i in range(n):
        x = arr[i]
        if not x in was:
            ret[i] = x
            was.add(x)
    left = sorted(list(can - was), reverse=True)
    for i in range(n):
        if not left:
            break
        x = left[-1]
        if not ret[i]:
            ret[i] = x
            left.pop()
    mx = ret[0]
    flag = True
    for i in range(n):
        mx = max(mx, ret[i])
        if mx != arr[i]:
            flag = False
            break
    if flag:
        print(*ret)
    else:
        print(-1)
