n = int(input())
num = 1
prex, prey = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    if prex == prey:
        num += min(x - prex, y - prey)
        prex, prey = x, y
    elif prex < prey:
        if x >= prey:
            prex = prey
            num += 1
            num += min(x - prex, y - prey)
            prex, prey = x, y
        else:
            prex, prey = x, y
    else:
        if y >= prex:
            prey = prex
            num += 1
            num += min(x - prex, y - prey)
            prex, prey = x, y
        else:
            prex, prey = x, y

print(num)
