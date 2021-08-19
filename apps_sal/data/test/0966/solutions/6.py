def check(x):
    return len(set(str(x))) == len(str(x))


y = int(input()) + 1
while not check(y):
    y += 1
print(y)
