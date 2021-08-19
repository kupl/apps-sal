def check(x):
    return len(set(str(x))) == len(str(x))


y = int(input()) + 1
while check(y) == 0:
    y += 1
print(y)
