n = int(input())
a = list(map(int, input().split()))
a_ = [i for i in a if i % 2 == 0]

for i in a_:
    bool_3 = i % 3 != 0
    bool_5 = i % 5 != 0
    if bool_3 and bool_5:
        print('DENIED')
        break
else:
    print('APPROVED')
