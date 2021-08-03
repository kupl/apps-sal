x = int(input())
l = divmod(x, 500)
m = l[0]
n = l[1] // 5
print(1000 * m + 5 * n)
