n = int(input())
a = [int(x) for x in input().split()]
a.sort()
counter = 0
i = 1
uk = 0
while uk < n:
    if a[uk] < i:
        uk += 1
    else:
        counter += 1
        uk += 1
        i += 1
print(counter)
