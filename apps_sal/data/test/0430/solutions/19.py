n = int(input())
M = sorted([int(x) // 100 for x in input().split()])
if sum(M) & 1:
    print('NO')
else:
    goal = sum(M) // 2
    if goal & 1:
        if M[0] == 1:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
