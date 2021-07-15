N,M = map(int,input().split())
if N*2 > M:
    print(M//2)
else:
    M -= N*2
    print(N+M//4)
