n = int(input())
A = list(map(int, input().split()))
cur1 = 0
cur2 = 0
cur3 = 0
p = 1
for i in range(len(A)):
    if A[i] == 25:
        cur1 += 1
    elif A[i] == 50:
        if cur1 == 0:
            print('NO')
            p = 0
            break
        else:
            cur1 -= 1
            cur2 += 1
    else:
        if cur2 >= 1 and cur1 >= 1:
            cur2 -= 1
            cur1 -= 1
            cur3 += 1
        elif cur1 >= 3:
            cur1 -= 3
            cur3 += 1
        else:
            print('NO')
            p = 0
            break
if p:
    print('YES')

