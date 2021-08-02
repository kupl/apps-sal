n = int(input())
a = list(map(int, input().split(' ')))
f = False
for j in range(len(a) - 2):
    #------------------------#
    for i in range(j, len(a) - 3):
        if a[j] < a[i + 2] < a[j + 1] < a[i + 3] or a[j] < a[i + 3] < a[j + 1] < a[i + 2] or a[i + 2] < a[j] < a[i + 3] < a[j + 1] or a[i + 3] < a[j] < a[i + 2] < a[j + 1] or a[j + 1] < a[i + 2] < a[j] < a[i + 3] or a[j + 1] < a[i + 3] < a[j] < a[i + 2] or a[i + 2] < a[j + 1] < a[i + 3] < a[j] or a[i + 3] < a[j + 1] < a[i + 2] < a[j]:
            f = True
            break
if f == True:
    print('yes')
else:
    print('no')
