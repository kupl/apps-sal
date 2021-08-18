N, M = [int(i) for i in input().split()]
X = [int(i) for i in input().split()]

if N >= M:
    print(0)
    return
Xs = sorted(X)
dst = []
for i in range(M - 1):
    dst.append(Xs[i + 1] - Xs[i])
# print(Xs)
# print(dst)
dsts = sorted(dst)
# print(dsts[:len(dsts)-N+1])
print(sum(dsts[:len(dsts) - N + 1]))
