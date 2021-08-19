
H, W = list(map(int, input().split()))
N = int(input())
S = list(map(int, input().split()))

T = [[0 for j in range(W)] for i in range(H)]
posx = 1
posy = 1
for i in range(N):
    tmp = S[i]
    cnt = 0
    while tmp > cnt:
        T[posy - 1][posx - 1] = i + 1
        if posy % 2 != 0:
            posx += 1
            if posx > W:
                posy += 1
                posx -= 1
        else:
            posx -= 1
            if posx < 1:
                posy += 1
                posx += 1
        cnt += 1

for i in T:
    print((*i))
