n = int(input())

lst = []
for x in input().split():
    lst.append(int(x))

sum_1 = 0
sum_2 = 0
for x in lst:
    if x >= 0:
        sum_1 += x
    else:
        sum_2 += x

print(sum_1 - sum_2)
