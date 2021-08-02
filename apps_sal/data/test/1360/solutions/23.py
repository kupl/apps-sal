n = int(input())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])
l.sort()
curDay = 0
for a, b in l:
    if b >= curDay:
        curDay = b
    else:
        curDay = a
print(curDay)
