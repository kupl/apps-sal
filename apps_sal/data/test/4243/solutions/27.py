x = int(input())
n500 = x // 500
n5 = (x % 500) // 5
print(n500 * 1000 + n5 * 5)
