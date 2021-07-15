d = [ [ [ 0 for i in range(51) ] for j in range(31) ] for g in range(31)]
def rec(n, m ,k):
    nonlocal d
    if k == 0 or n*m == k:
        return 0
    if d[n][m][k] > 0 :
        return d[n][m][k]
    if n * m < k:
        return 10 ** 10
    cost  = 10**10
    for i in range(1, n//2 +1):
        for j in range(k+1):
            cost = min(cost, m**2 + rec(i, m, j) + rec(n-i, m, k-j))
    for i in range(1, m//2 +1):
        for j in range(0, k+1):
            cost = min(cost, n**2 + rec(n, i, j) + rec(n, m-i, k-j))
    d[n][m][k] = cost
    return cost
t = int(input())
a = []
for c in range(t):
    n, m ,k = map(int, input().split())
    a.append(rec(n,m,k))
print('\n'.join(str(x) for x in a))
