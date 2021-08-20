K = int(input())
x = K // 50
print(50)
print(*(50 - (K - 50 * x)) * [49 - K + 51 * x] + (K - 50 * x) * [100 - K + 51 * x])
