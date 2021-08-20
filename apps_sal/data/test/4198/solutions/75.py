(a, b, x) = map(int, input().split())
upper = 10 ** 9 + 1
bottom = 0
while upper - bottom > 1:
    middle = (upper + bottom) // 2
    if a * middle + b * len(str(middle)) <= x:
        bottom = middle
    else:
        upper = middle
print(bottom)
