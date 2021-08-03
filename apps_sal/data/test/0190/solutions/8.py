n, m = [int(x) for x in input().split()]
minX = m + 1
maxX = -1
minY = n + 1
maxY = -1
for i in range(n):
    line = input()
    j = 0
    for c in line:
        if c == '*':
            if minX > j:
                minX = j
            if maxX < j:
                maxX = j
            if minY > i:
                minY = i
            if maxY < i:
                maxY = i
        j += 1

print(max(maxX - minX + 1, maxY - minY + 1))
