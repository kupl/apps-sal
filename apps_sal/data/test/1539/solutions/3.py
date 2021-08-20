n = int(input())
INF = -1
arr = [0] * n
d = [0] * 201
l = list(map(int, input().split()))
e = list(map(int, input().split()))
s = 0
for i in range(n):
    arr[i] = (l[i], e[i])
    s += e[i]
    d[e[i]] += 1
l = []
e = []
ans = [INF] * 3
ans[2] = 10 ** 10
p = arr[-1][0]
k = [0, 0]
arr.sort()
arr = [(-1, -1)] + arr
e = 0
c = 0
for i in range(n, -1, -1):
    if arr[i][0] == p:
        c += 1
        e += arr[i][1]
        d[arr[i][1]] -= 1
    else:
        if c == 1:
            ans[0] = max(ans[0], e)
        elif c == 2:
            ans[1] = max(ans[1], arr[i + 1][1] + arr[i + 2][1])
        if c >= 2:
            mx = c + c - 1
            eng = k[1]
            if k[0] >= n - mx:
                ans[2] = min(ans[2], eng)
            else:
                g = n - mx - k[0]
                j = 1
                while j < 201 and g > 0:
                    if d[j] > 0:
                        if g > d[j]:
                            eng += d[j] * j
                            g -= d[j]
                        else:
                            eng += g * j
                            g = 0
                    j += 1
                if g == 0:
                    ans[2] = min(ans[2], eng)
        k[0] += c
        k[1] += e
        c = 1
        e = arr[i][1]
        d[arr[i][1]] -= 1
        p = arr[i][0]
mn = 10 ** 10
for i in range(2):
    ans[i] = s - ans[i]
for i in range(3):
    if ans[i] != -1 and mn > ans[i]:
        mn = ans[i]
if mn != 10 ** 10:
    print(mn)
else:
    print(0)
