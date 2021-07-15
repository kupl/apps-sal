import itertools

N, M = map(int, input().split())
L = []
res, cnt = 0, 1

for i in range(N):
    K = list(map(int, input().split()))
    L.append(K[1:])

L = list(itertools.chain.from_iterable(L))
L.sort()
L.append(100)

for i in range(len(L)-1):
    if L[i] == L[i+1]:
        cnt += 1
    else:
        if cnt == N:
            res += 1
        cnt = 1
    

print(res)
