n, k = map(int, input().split())
k = min(k, n)
if k % 2 == 1:
    k -= 1
if k == 0:
    print(0)
else:
    half_k = k >> 1
    prices = []
    for _ in range(n):
        prices.append(int(input()))
    minimi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                minimi[i][j] = prices[j]
            else:
                minimi[i][j] = min(minimi[i][j - 1], prices[j])
    tabella = [[0 for _ in range(n)] for _ in range(half_k)]
    for j in range(1, n):
        tabella[0][j] = max(prices[j] - minimi[0][j - 1], tabella[0][j - 1])
    for i in range(1, half_k):
        for j in range(1, n):
            tabella[i][j] = max(tabella[i][j - 1], tabella[i - 1][j])
            appo = 0
            for k in range(j - 1):
                appo = max(appo, tabella[i - 1][k] + prices[j] - minimi[k + 1][j - 1])
            tabella[i][j] = max(tabella[i][j], appo)
    print(tabella[-1][-1])
