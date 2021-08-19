(n, x, y) = list(map(int, input().split()))
for i in range(n):
    hit = int(input())
    vayna_hits_rate = int(x * (hit + 1) / (x + y)) / x
    voya_hits_rate = int(y * (hit + 1) / (x + y)) / y
    if vayna_hits_rate == voya_hits_rate:
        print('Both')
    elif vayna_hits_rate > voya_hits_rate:
        print('Vanya')
    else:
        print('Vova')
