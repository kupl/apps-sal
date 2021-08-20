X = int(input())
num_500 = X // 500
num_5 = X % 500 // 5
grad = num_500 * 1000 + num_5 * 5
print(grad)
