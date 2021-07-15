n = int(input())
a = [int(_) for _ in input()]

num = len([_ for _ in a if _ == 8])
length = len(a)

print(min(length // 11, num))

