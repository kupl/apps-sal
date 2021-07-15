from itertools import product

def relax(D, t):
    k, i, j = t
    D[i][j] = min(D[i][j], D[i][k] + D[k][j])

N = int(input())
D = list([list(map(int, input().split())) for i in range(N)])
list([relax(D, t) for t in product(list(range(N)), list(range(N)), list(range(N)))])
print(max(list(map(max, D))))

