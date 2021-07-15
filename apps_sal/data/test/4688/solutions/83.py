def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lint(): return list(map(int, input().split()))
def lint_dec(): return list([int(x) - 1 for x in input().split()])
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [int(input()) for _ in range(n)]
def graph_input(G, m):
    for _ in range(m):
        a, b = lint_dec()
        G[a].append(b)
        G[b].append(a)



############################################################
N, K = lint()
print((K * pow(K - 1, N - 1)))

