X = int(input())
yen500, yen5 = divmod(X, 500)
yen5 = yen5 // 5
print(yen500 * 1000 + yen5 * 5)
