n, k = map(int, input().split())
V = list(map(int, input().split()))

ans = - 10 ** 19
# i: Dから取り出す宝石の個数
for i in range(min(k + 1, n + 1)):
    # j: 左からとる個数(i-jが右からとる個数)
    for j in range(i + 1):
        inhands = V[:j] + V[n - i + j:]
        inhands.sort()
        remnum = k - i
        val = 0
        for h in inhands:
            if h < 0 and remnum > 0:
                remnum -= 1
            else:
                val += h
        ans = max(ans, val)
print(ans)
