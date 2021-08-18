import bisect

n = int(input())
li = [int(input()) for i in range(n)]
li = [-x for x in li]

X = []
X.append(li[0])

for i in range(1, n):
    idx = bisect.bisect_right(X, li[i])
    if idx == len(X):
        X.append(li[i])
    else:
        X[idx] = li[i]

print(len(X))
