N, K = list(map(int, input().split()))
H = list(map(int, input().split()))


if(len(H) > K):
    print((sum(sorted(H)[0:len(H)-K])))
else:
    print((0))

