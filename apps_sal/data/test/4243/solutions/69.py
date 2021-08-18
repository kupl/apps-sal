X = int(input())
h1000 = int(X / 500)
h5 = int((X % 500) / 5)
print(h1000 * 1000 + h5 * 5)
