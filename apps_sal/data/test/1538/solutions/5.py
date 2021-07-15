N = int(input())
boxes = sorted(list(map(int,input().split())))

high = 0
for item in boxes:
    high = max(high, boxes.count(item))

print(high)

