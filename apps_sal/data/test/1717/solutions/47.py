n = int(input())
l = [0, 1, 2, 3, 2, 5, 1, 7, 2, 3, 1, 11, 1, 13, 1, 1, 2, 17, 1, 19, 1, 1, 1, 23, 1, 5, 1, 3, 1, 29, 1]
product = 1
for i in range(1, n + 1):
    product *= l[i]
print(product + 1)
