m, d = list(map(int, input().split()))

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(((days[m] + d - 1) + 6) // 7)
