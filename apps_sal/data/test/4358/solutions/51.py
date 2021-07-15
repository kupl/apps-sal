N = int(input())
p = list(int(input()) for i in range(N))

# 合計支払金額を (整数として) 出力せよ。
# 注意：1版高い商品は半額

print(sum(p) - max(p) // 2)
