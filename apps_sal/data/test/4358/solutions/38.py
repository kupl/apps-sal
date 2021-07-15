N = int(input())
P = [int(input()) for _ in range(N)]

sortP = sorted(P)
ans = sum(sortP[:-1]) + sortP[-1]/2
print((int(ans)))

