def mi():
    return list(map(int, input().split()))


'''

'''
y, b, r = mi()
if b >= r:
    b = r - 1
else:
    r = b + 1
if y >= b:
    y = b - 1
else:
    b = y + 1
    r = b + 1
print(y + r + b)
