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
        h[i] = (y - h[i] + 1)
    """
tmp = h[-1]
for i in reversed(range(n-1)):
    if h[i]<=tmp:
        a.append(tmp-h[i]+1)
        tmp = max(tmp,h[i])
    else:a.append(0)"""
print(' '.join(map(str, (h))))
