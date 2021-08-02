n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
ans = []
# n冊の本において買うか買わないかの2通りなので2**n
for i in range(2**n):
    # リストの中身は値段1と理解度m個
    a = [0] * m
    price = 0
    for j in range(n):
        # n冊あるうちj冊目を買うか買わないかを判定
        if ((i >> j) & 1):
            for k in range(m):
                a[k] += c[j][k + 1]
            # j冊めを買うので、合計金額を増やす
            price += c[j][0]
    if all(j >= x for j in a):
        ans.append(price)

if len(ans) == 0:
    print("-1")
else:
    print(min(ans))
