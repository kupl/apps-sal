n = int(input())
data = list(map(int, input().split()))
places = dict()
i = 0
count = 0
check = True
for num in data:
    if num == i:
        count += 1
    elif check:
        if num in places:
            if places[num] == i:
                count += 2
                check = False
            else:
                places[i] = num
        else:
            places[i] = num
    i += 1
if check and count + 1 <= n:
    print(count + 1)
else:
    print(count)
