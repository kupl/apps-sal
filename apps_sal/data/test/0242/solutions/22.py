def f(num):
    temp = 0
    while num % 5 == 0:
        num //= 5
        temp += 1
    return temp


m = int(input())
num = 0
i = 5
while 500001 > i and m > num:
    num += f(i)
    i += 5
if m == num:
    print(5)
    i -= 5
    for j in range(5):
        print(i + j, end=' ')
else:
    print(0)
