n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i % 2 == 0:
        if i % 3 != 0 and i % 5 != 0:
            print('DENIED')
            break
else:
    print('APPROVED')
