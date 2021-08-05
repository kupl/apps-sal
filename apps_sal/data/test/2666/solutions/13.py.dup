n, k = map(int, input().split())
k = k // 2
l = []
for _ in range(n):
    l.append(int(input()))


def fip(p, no, kt):
    pr = [[0 for i in range(n + 1)] for j in range(k + 1)]

    #print("pr bef:\n",pr)
    for i in range(1, k + 1):
        pd = float('-inf')

        for j in range(1, n):

            #print("\ni,j:",i,j,"\ncomparing:pd",pd,"--and pr[i-1][j-1]  - p[j                -1]",pr[i-1][j-1],"-",p[j-1])
            pd = max(pd, pr[i - 1][j - 1] - p[j - 1])

            # print("pr[i][j] by comparing : pr[i][j-1],p[j]+pd ka max:",pr[i][j                -1],p[j],"+",pd)
            pr[i][j] = max(pr[i][j - 1], p[j] + pd)

            # print("pr:",pr)

    #print("pr aft:\n",pr)
    return pr[k][n - 1]


print(fip(l, n, k))
