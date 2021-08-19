r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))
a = [0] * 3
b = [0] * 3
for i in range(101):
    a[0] = i
    for j in range(3):
        b[j] = r1[j] - a[0]
    a[1] = r2[0] - b[0]
    a[2] = r3[0] - b[0]
    flag = False
    for j in range(3):
        if r1[j] == a[0] + b[j] and r2[j] == a[1] + b[j] and (r3[j] == a[2] + b[j]):
            flag = True
        else:
            flag = False
            break
    if flag:
        break
print('Yes') if flag else print('No')
