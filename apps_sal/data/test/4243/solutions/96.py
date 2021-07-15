X = int(input())
happy500 = X // 500
happy5 = (X - (happy500 * 500)) // 5
answer = happy500 * 1000 + happy5 * 5
print(answer)
