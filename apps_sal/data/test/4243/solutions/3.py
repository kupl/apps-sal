X = int(input())
thousand = X // 500
rest = X - thousand * 500
five = rest // 5
print(1000 * thousand + 5 * five)
