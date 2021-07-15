n = int(input())
x1, x2, x3 = list(map(int, input().split()))
y1, y2, y3 = list(map(int, input().split()))
max1, min1 = min(x1, y2)+min(x2, y3)+min(x3, y1), 0
if x1 > y1+y3:
    min1 = x1-y1-y3
elif x2 > y2+y1:
    min1 = x2-y1-y2
elif x3 > y3+y2:
    min1 = x3-y3-y2
print(min1, max1)

