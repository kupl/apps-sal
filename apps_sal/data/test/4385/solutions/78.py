cor = [0 for i in range(5)]
for i in range(5):
    cor[i] = int(input())
k = int(input())
flag = True
for i in range(5):
    for j in range(i, 5):
        if abs(cor[i] - cor[j]) > k:
            flag = False
if flag:
    print('Yay!')
else:
    print(':(')
