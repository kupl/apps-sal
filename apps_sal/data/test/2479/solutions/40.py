N, Q = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]
ans = 0

for T in range(1, 3):
    Depth = [N-2]*N
    left = N
    up = N-2
    for t, x in Query:
        if t == T:  # |
            if left < x:
                ans += Depth[x]
            else:
                for i in range(x, left):
                    Depth[i] = up
                left = x
                ans += up
        else:  # -
            up = min(up, x-2)
        #print(f"ans={ans}, up={up}")
    #print("---")

print(((N-2)**2-ans))

