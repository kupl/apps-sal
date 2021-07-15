n, m = map(int, input().split())
count = n
day = 1
while count != 0:
    count -= 1
    if day % m == 0:
        count += 1
    if count!=0:
        day+=1
print(day)
