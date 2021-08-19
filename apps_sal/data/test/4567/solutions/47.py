n = int(input())
sum = 0
point = []
for i in range(n):
    now = int(input())
    point.append(now)
    sum += now
#point = list(map(int, input()))
if sum % 10 != 0:
    print(sum)
else:
    point.sort()
    judge = False
    for i in point:
        if i % 10 != 0:
            point.remove(i)
            sum -= i
            judge = True
            break
    if judge:
        print(sum)
    else:
        print((0))
