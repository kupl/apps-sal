n = int(input())
n *= 2
lst = input().split(' ')
for m in range(0, n):
    lst[m] = eval(lst[m])
for i in range(0, n):
    for j in range(0, n - i - 1):
        if lst[j] < lst[j + 1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp
result = 0
for k in range(0, n):
    if k % 2 == 1:
        result += lst[k]
print(result)
