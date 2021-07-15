x = int(input())
flag = True
while flag:
    flag = False
    for i in range(2, x):
        if x%i == 0:
            flag = True
            x += 1
            break
print(x)
