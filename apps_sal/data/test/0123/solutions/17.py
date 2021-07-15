n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if k > 1:
    print('Yes')
    return
else:
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = b[0]
            break
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            print('Yes')
            return
print('No')

