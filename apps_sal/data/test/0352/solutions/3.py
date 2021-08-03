n = int(input())
min1, max1 = map(int, input().split(" "))
min2, max2 = map(int, input().split(" "))
min3, max3 = map(int, input().split(" "))
x1 = min(n - min3 - min2, max1)
n -= x1
x2 = min(n - min3, max2)
x3 = n - x2
print(x1, x2, x3)
