num = input()
le = len(num)
num2 = [0] * le
for i in range(le):
    num2[i] = int(num[i])
print(max(num2))
for i in range(le):
    while num2[i] > 0:
        print(1, end='')
        for j in range(i + 1, le):
            if num2[j] > 0:
                num2[j] -= 1
                print(1, end='')
            else:
                print(0, end='')
        print(' ', end='')
        num2[i] -= 1
