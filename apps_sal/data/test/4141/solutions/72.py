N = int(input())
A = list(map(int, input().split()))
for i in A:
    if i % 2 == 0 and (i % 3 == 0 or i % 5 == 0):
        continue
    elif i % 2 == 1:
        continue
    else:
        print('DENIED')
        return
print('APPROVED')
