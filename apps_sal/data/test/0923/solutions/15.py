
N = int(input())
G = list(map(int, input().split()))
real = [i for i in range(N)]
d = [1, -1]

if G == real:
    print('Yes')
else:
    for i in range(N):
        for j in range(N):
            G[j] = real[(G[j] + d[j % 2]) % N]
        if G == real:
            print('Yes')
            break
    else:
        print('No')
