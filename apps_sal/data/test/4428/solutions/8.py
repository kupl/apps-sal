n = int(input())
ls = [int(i) for i in input().split()]

if n == 1:
    print(0)
    return

f1, f2 = 0, n - 1

ans = 0
sum1, sum2 = ls[0], ls[n - 1]
if sum1 == sum2:
    ans = sum1
    f1 += 1
    sum1 += ls[f1]

while True:
    while sum1 != sum2 and f1 + 1 < f2:
        if sum1 < sum2:
            f1 += 1
            sum1 += ls[f1]
        else:
            f2 -= 1
            sum2 += ls[f2]

    if sum1 == sum2:
        ans = sum1
        if f1 + 1 >= f2:
            break
        f1 += 1
        sum1 += ls[f1]
    else:
        break

print(ans)
