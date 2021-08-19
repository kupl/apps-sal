def check(x):
    return len(set(str(x))) == len(str(x))


y = int(input()) + 1
while check(y) == False:
    y += 1
print(y)
