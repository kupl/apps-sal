a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(a) > len(b):
    print('GREATER')
    return
elif len(a) < len(b):
    print('LESS')
    return
else:
    for i in range(len(a)):
        if a[i] > b[i]:
            print('GREATER')
            return
        elif a[i] < b[i]:
            print('LESS')
            return
print('EQUAL')
