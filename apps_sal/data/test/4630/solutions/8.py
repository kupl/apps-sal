q = int(input())
for i in range(q):
    n = int(input())
    lis = [0] * n
    a = list(map(int, input().split()))
    q = []
    ind = 0
    now = 0
    end = 0
    while end < n:
        while ind < n:
            if lis[ind] == 0:
                now = ind
                break
            ind += 1
        q = []
        while len(q) == 0 or now != q[0]:
            q.append(now)
            now = a[now] - 1
        for i in q:
            lis[i] = len(q)
        end += len(q)
    print(' '.join(map(str, lis)))
