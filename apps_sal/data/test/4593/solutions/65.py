from bisect import bisect_right


cands = []
for i in range(2, 400):
    cur = i
    while cur * i <= 1000:
        cands.append(cur * i)
        cur *= i
cands.sort()

X = int(input())
if X == 1:
    print((1))
else:
    print((cands[bisect_right(cands, X) - 1]))

