import sys

h, w, n = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]

dict = {}
ans = [0] * 10
ans[0] = (w - 2) * (h - 2)

for item in A:
    cord = list(item)
    upcand = []
    for i in range(cord[0] - 1, cord[0] + 2):
        for j in range(cord[1] - 1, cord[1] + 2):
            upcand.append([i, j])
    for cand in upcand:
        if 1 < cand[0] < h and 1 < cand[1] < w:
            dict[(cand[0], cand[1])] = dict.get((cand[0], cand[1]), 0) + 1
for v in list(dict.values()):
    ans[v] += 1
    ans[0] -= 1

for i in ans:
    print(i)
