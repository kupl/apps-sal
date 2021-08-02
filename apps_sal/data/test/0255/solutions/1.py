n = int(input())
boys = [int(x) for x in input().split()]
m = int(input())
girls = [int(x) for x in input().split()]

# we sort the lads
boys.sort()
girls.sort()

count = 0
last_girl = -1

for boy in boys:
    # try to find a match, if we find, we increment the namber
    for gi in range(last_girl + 1, len(girls)):
        girl = girls[gi]
        if (girl + 1 == boy) or girl == boy or girl - 1 == boy:
            count += 1
            last_girl = gi
            break

print(count)
