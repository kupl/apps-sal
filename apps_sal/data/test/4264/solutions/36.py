n = int(input())
# n個の整数のリスト
num_list = []
# 偶数の桁数の整数のリスト
num_odd_list = []

# n個の整数のリストに代入
for i in range(1, n + 1):
    num_list.append(i)

# 偶数の桁数の整数をリストに代入
for j in num_list:
    if 10 <= j < 100 or 1000 <= j < 10000 or 100000 <= j < 1000000:
        num_odd_list.append(j)

# 全体の整数の数から偶数の桁数の整数の数を引く
print(len(num_list) - len(num_odd_list))
