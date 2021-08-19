n = int(input())
h = list(map(int, input().split()))
a = []
if n == 1:
    print(0)
    quit()
y = h[-1]
h[-1] = 0
for i in reversed(range(n - 1)):
    if h[i] > y:
        y = max(h[i], y)
        h[i] = 0
        h[-1] = 0
    else:
        h[i] = y - h[i] + 1
    '\ntmp = h[-1]\nfor i in reversed(range(n-1)):\n    if h[i]<=tmp:\n        a.append(tmp-h[i]+1)\n        tmp = max(tmp,h[i])\n    else:a.append(0)'
print(' '.join(map(str, h)))
