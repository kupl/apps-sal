a = int(input()) + 1
b = sum(list(map(int, input().split())))
print(len([i for i in [1, 2, 3, 4, 5] if (i + b) % a != 1]))
