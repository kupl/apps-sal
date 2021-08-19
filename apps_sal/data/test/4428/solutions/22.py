length = int(input())
numbers = list(map(int, input().split(' ')))
lastResult = 0
(sum1, sum3) = (0, 0)
(i1, i3) = (0, length - 1)
while True:
    if i1 > i3:
        break
    if sum1 < sum3:
        sum1 += numbers[i1]
        i1 += 1
    elif sum1 > sum3:
        sum3 += numbers[i3]
        i3 -= 1
    else:
        lastResult = sum1
        sum1 += numbers[i1]
        i1 += 1
print(sum1 if sum1 == sum3 else lastResult)
