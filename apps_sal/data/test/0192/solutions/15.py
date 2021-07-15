def exists(a, b, c):
    return a < b + c and b < a + c and c < a + b

x, y = [int(i) for i in input().split()]
a, b, c = y, y, y
count = 0
while a != x or b != x or c != x:
    a, b, c = sorted([a, b, c])
    a = x if exists(x, b, c) else b + c - 1
    count += 1
    
print(count)
