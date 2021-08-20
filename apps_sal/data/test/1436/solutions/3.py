n = int(input())
count = 0
free = 0
t = [int(x) for x in input().split()]
for i in t:
    if i > 0:
        free += i
    if i == -1:
        if free > 0:
            free -= 1
        else:
            count += 1
print(count)
