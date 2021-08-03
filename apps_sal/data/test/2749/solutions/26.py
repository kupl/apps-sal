from collections import defaultdict
h, w = list(map(int, input().split()))
n = int(input())
a = list(map(int, input().split()))

ans = [0] * h
for i in range(h):
    ans[i] = [0] * w

b = []
for i in range(n):
    for k in range(a[i]):
        b.append(i + 1)

hidx = 0
widx = 0
for i in range(len(b)):
    ans[hidx][widx] = b[i]
    if hidx % 2 == 0:
        widx += 1
    else:
        widx -= 1
    if widx == w:
        widx = -1
        hidx += 1
    if widx == -(w + 1):
        widx = 0
        hidx += 1

for i in range(h):
    answer = ans[i]
    L = [str(a) for a in answer]
    L = " ".join(L)
    print(L)
