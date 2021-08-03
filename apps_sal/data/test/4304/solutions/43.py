lst = input().split()
a = int(lst[0])
b = int(lst[1])

d = b - a

print(sum(range(1, d + 1)) - b)
