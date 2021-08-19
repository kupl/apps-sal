a = []
for i in range(3):
    a.extend(list(map(int, input().split())))
n = int(input())
b = []
cnt = []
pattern = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
for i in range(n):
    b.append(int(input()))
    for (j, x) in enumerate(a):
        if x == b[i]:
            cnt.append(j)
for (q, w, e) in pattern:
    if q in cnt and w in cnt and (e in cnt):
        print('Yes')
        break
else:
    print('No')
