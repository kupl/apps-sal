# 入力の整数列を取得する
n = int(input())
nums = list(map(int, input().split()))

# 逆数のリストを作成する
re_nums = [1 / num  for num in nums]

# 逆数のリストの総和の逆数を求める
print(1 / sum(re_nums))
