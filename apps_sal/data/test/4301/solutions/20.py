N = int(input())
b = []
max_num = 0
for i in range(N):
    a = int(input())
    b.append(a)
    max_num = max(a, max_num)
max_num2 = 0
num = b.count(max_num)
if num > 1:
    for i in range(N):
        print(max_num)
elif num == 1:
    for i in b:
        if i == max_num:
            pass
        else:
            max_num2 = max(max_num2, i)
    for i in b:
        if max_num == i:
            print(max_num2)
        else:
            print(max_num)
