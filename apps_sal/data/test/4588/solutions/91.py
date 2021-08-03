array = ["A", "B", "C", "D", "E", "F"]
X, Y = input().split()
print("<") if array.index(X) < array.index(Y) else print(">") if array.index(X) > array.index(Y) else print("=")
