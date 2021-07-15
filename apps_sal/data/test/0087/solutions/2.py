m, d = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(-(-(month[m - 1] + d - 1) // 7))
