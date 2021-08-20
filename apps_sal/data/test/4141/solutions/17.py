n = int(input())
a = list(map(int, input().split()))
flag = True
for i in a:
    if i % 2 == 0:
        if not (i % 3 == 0 or i % 5 == 0):
            flag = False
            break
print('APPROVED' if flag else 'DENIED')
