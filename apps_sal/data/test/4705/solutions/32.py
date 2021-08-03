# 定義 1 <= N <= 100

N = int(input())

x = 800 * N
y = (N // 15) * 200

payment = x - y
print(payment)
