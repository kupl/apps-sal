n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
m = 0
temp = 1
if len(a) > 1:
    for i in range(1, n):
        if a[i] == a[i - 1]:
            temp = 1
        else:
            temp += 1

        if temp > m:
            m = temp
else:
    m = 1

print(m)
