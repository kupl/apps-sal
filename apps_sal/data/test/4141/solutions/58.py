# 入力を取得する
n = int(input())
nums = list(map(int, input().split()))

# 奇数を除く
evens = [num for num in nums if num % 2 == 0]

# 3 と 5で割って余りが0ならば入国を承認
approved = all([even % 3 == 0 or even % 5 == 0 for even in evens])
print("APPROVED " if approved else "DENIED")
