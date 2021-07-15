a, b, c = map(int, input().split())
list01 = [a, b, c]
list02 = sorted(list01)
print(list02[2] - list02[1] + list02[1] - list02[0])
