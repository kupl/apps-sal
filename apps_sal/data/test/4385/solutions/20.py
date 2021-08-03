a = []
for i in range(5):
    a.append(int(input()))
k = int(input())
isOK = True
for i in range(5):
    for j in range(i + 1, 5):
        if abs(a[i] - a[j]) > k:
            isOK = False
            break
if isOK:
    print('Yay!')
else:
    print(':(')
