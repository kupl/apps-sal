# 入力を受け取る
N,L = map(int, input().split())

# 数列を作成する
nums = list(range(1,N+1))
tasts = [L+num-1 for num in nums]

# 味の絶対値が最も小さいリンゴのindexを特定する
abs_tasts = list(map(abs,tasts))
index = abs_tasts.index(min(abs_tasts))
tasts.pop(index)

# 上記リンゴを除いた残りのリンゴの味の総和を求める
print(sum(tasts))
