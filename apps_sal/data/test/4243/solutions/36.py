x = int(input())
m = divmod(x, 500)
print(m[0] * 1000 + m[1] // 5 * 5)
