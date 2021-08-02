md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d = list(map(int, input().split()))
fsl = 7 - d + 1
md[m - 1] -= fsl
print(1 - (-md[m - 1] // 7))
