import sys

input = sys.stdin.readline

def main():
    H, W = list(map(int, input().split()))
    field = []
    odd = []
    for i in range(H):
        tmp = list(map(int, input().split()))
        field.append(tmp)
    
    rote = []
    for h in range(H):
        for j in range(W):
            if h%2 == 1:
                w = W-j-1
            else:
                w = j
            rote.append((h, w))
    
    ans = []
    for i, r in enumerate(rote):
        h, w = r
        if field[h][w] % 2 == 1:
            if i == H*W-1:
                break
            s, t = rote[i+1]
            ans.append((h+1, w+1, s+1, t+1))
            field[h][w] -= 1
            field[s][t] += 1

    print((len(ans)))
    for a in ans:
        print((*a))

def __starting_point():
    main()

__starting_point()
