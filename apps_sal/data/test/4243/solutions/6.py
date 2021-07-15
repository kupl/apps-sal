X = int(input())

num_500 = X // 500
num_5 = (X - 500 * num_500) // 5

print(1000 * num_500 + 5 * num_5)
