import sys

H, W, M = list(map(int, input().split()))
A = [list([int(x) - 1 for x in input().split()]) for i in range(M)]

cnth = [0] * H
cntw = [0] * W
st = set()

for y, x in A:
    cnth[y] += 1
    cntw[x] += 1
    st.add((y, x))

my = max(cnth)
mx = max(cntw)

Y = []
X = []

for i in range(H):
    if cnth[i] == my:
        Y.append(i)

for i in range(W):
    if cntw[i] == mx:
        X.append(i)

for y in Y:
    for x in X:
        if not (y, x) in st:
            print((my + mx))
            return

print((my + mx - 1))
