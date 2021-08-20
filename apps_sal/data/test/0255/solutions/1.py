n = int(input())
boys = [int(x) for x in input().split()]
m = int(input())
girls = [int(x) for x in input().split()]
boys.sort()
girls.sort()
count = 0
last_girl = -1
for boy in boys:
    for gi in range(last_girl + 1, len(girls)):
        girl = girls[gi]
        if girl + 1 == boy or girl == boy or girl - 1 == boy:
            count += 1
            last_girl = gi
            break
print(count)
