m, d = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = (d - 1 + month[m - 1])
if res % 7 > 0:
    print(res // 7 + 1)
else:
    print(res // 7)
