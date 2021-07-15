def solve(g):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:continue
            for p in range(n):
                for q in range(n):
                    if p == i or q == j:continue
                    if g[i][q] + g[p][j] == g[i][j]:break
                else:
                    continue
                break
            else:
                return "No"
    return "Yes"

n = int(input())

g = []

for i in range(n):
    g.append([int(item) for item in input().split()])
    
print(solve(g))
