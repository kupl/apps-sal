(a1, a2, a3, a4) = map(int, input().split())
a = list(map(int, input()))
sum = 0
for i in range(len(a)):
    if a[i] == 1:
        sum += a1
    elif a[i] == 2:
        sum += a2
    elif a[i] == 3:
        sum += a3
    else:
        sum += a4
print(sum)
