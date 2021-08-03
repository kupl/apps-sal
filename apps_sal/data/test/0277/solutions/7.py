n, a, b = list(map(int, input().split()))
flag = 2
a -= 1
b -= 1
i = 1
while flag < n:
    if a // flag == b // flag:
        print(i)
        break
    i += 1
    flag *= 2
else:
    print('Final!')
