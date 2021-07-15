D, G = map(int,input().split())
table = []
ans = 0

for i in range(D):
    p,c = map(int,input().split())
    ans += p
    table.append((p,c))


for i in range(2**D):
    score = 0
    n = 0
    solved = [0] * D
    for j in range(D):
        if i>>j & 1:
            p,c = table[j]
            solved[j] = 1
            score += 100*(j+1)*p+c
            n += p
    if score<G:
        for k in range(D-1,-1,-1):
            if solved[k] == 0:
                p = table[k][0]
                for l in range(1,p):
                    score += 100*(k+1)
                    n += 1
                    if score>=G:
                        break
                break

    if score>=G:
        ans = min(n,ans)
print(ans)
