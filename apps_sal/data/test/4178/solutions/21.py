n = int(input())
h = list(map(int, input().split()))
h[0] -= 1
for i in range(1, n):
    if h[i - 1] < h[i]:
        h[i] -= 1
l = list(h)
l.sort()
if h == l:
    print('Yes')
else:
    print('No')
