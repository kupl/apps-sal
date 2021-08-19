U = int(input())
D = int(input())
last = max(1, 1 + D)
next = last
print(last, end=' ')
while U > 0:
    last += 1
    print(last, end=' ')
    U -= 1
while D > 0:
    next -= 1
    print(next, end=' ')
    D -= 1
