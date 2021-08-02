n = int(input())

numbers = [int(i) for i in input().split(" ")]

s = 0
a = 0
sum1 = 0
b = n - 1
sum2 = 0
while a <= b:
    if sum1 < sum2:
        sum1 += numbers[a]
        a += 1
    else:
        sum2 += numbers[b]
        b -= 1

    if sum1 == sum2:
        s = sum1

print(s)
