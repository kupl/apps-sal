N = int(input())
A = list(map(int, input().split()))
j = 0
for i in A:
    if i % 2 == 0:
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            j += 1
    else:
        pass
if j > 0:
    print('DENIED')
else:
    print('APPROVED')
