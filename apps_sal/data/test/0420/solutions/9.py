n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append(input())
result = n
flag = True
while n % 2 == 0:
    n = int(n / 2)
    x1 = n
    x2 = n + 1
    while x1 > 0:
        if a[x1 - 1] != a[x2 - 1]:
            flag = False
            break
        x1 -= 1
        x2 += 1
    if flag == False:
        break
    result = n


print(result)

