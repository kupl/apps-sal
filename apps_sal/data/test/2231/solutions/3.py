import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(set(a)) == 1:
        print(a[0], a[0], a[0], a[0])
    else:
        a.sort()
        g1 = False
        d = {}
        mx = 10001
        for i in a:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
            if d[i] == 4:
                g1 = True
                if i < mx:
                    mx = i
        if g1:
            print(mx, mx, mx, mx)
        else:
            res = []
            for k in d.keys():
                if d[k] >= 2:
                    res.append(k)
            m = len(res)
            minj = 0
            for j in range(m - 1):
                if res[j] * res[j + 1] * (res[minj] ** 2 + res[minj + 1] ** 2) > res[minj] * res[minj + 1] * (res[j] ** 2 + res[j + 1] ** 2):
                    minj = j
            print(res[minj], res[minj], res[minj + 1], res[minj + 1])
