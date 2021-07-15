def main():
    n = int(input())
    B = []
    g = [[0]*(2*n) for _ in range(2*n)]
    for _ in range(n):
        a,b  = map(int,input().split())
        g[b][a] = 1
    for _ in range(n):
        c,d = map(int,input().split())
        B.append((c,d))
    B.sort()
    ans = 0
    for i,j in B:
        f = 0
        for y in range(j,-1,-1):
            for x in range(i,-1,-1):
                if g[y][x]:
                    ans += 1
                    f = 1
                    g[y][x] = 0
                    break
            if f:
                break
    print(ans)

main()
