n = int(input())

x = [0] * n
y = [0] * n
h = [0] * n

for i in range(n):
    x[i], y[i], h[i] = map(int, input().split())

for cx in range(101):
    for cy in range(101):
        H = -1
        for i in range(n):
            if h[i] == 0:
                pass
            else:
                tmp = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                H = tmp
                break
        flag = True
        for i in range(n):
            if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                flag = False
                break
        if flag:
            print(cx, cy, H)
