n = int(input())

sum = 0
for i in range(n):
    x1, y1, x2, y2  = [int(c) for c in input().split()]
    sum += (x2 - x1 + 1)*(y2-y1 + 1)
print(sum)



