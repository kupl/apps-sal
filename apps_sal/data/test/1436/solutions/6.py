n = int(input())
seq = list(map(int, input().split()))
avail_cops = 0
crimes = 0
for event in seq:
    if event > 0:
        avail_cops += event
    elif avail_cops == 0:
        crimes += 1
    else:
        avail_cops -= 1
print(crimes)
