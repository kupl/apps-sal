(n, x, y) = list(map(int, input().split()))
l1 = list(map(int, input().split()))
count1 = 0
count2 = 0
for item in l1:
    if item <= x:
        count1 += 1
        if item + y > x:
            count2 += 1
if x > y:
    print(n)
elif x == y:
    if count1 % 2 == 0:
        print(count1 // 2)
    else:
        print(count1 // 2 + 1)
else:
    total = 0
    if count2 % 2 == 0:
        total += count2 // 2
    else:
        total += count2 // 2 + 1
    print(total + (count1 - count2))
