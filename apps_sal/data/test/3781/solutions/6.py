from collections import Counter
T = int(input())
for i in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    if N % 2 == 1:
        print('Second')
    else:
        flag = 0
        c = Counter(a)
        val = list(c.values())
        for j in val:
            if j % 2 == 1:
                flag = 1
                break
        if flag == 1:
            print('First')
        else:
            print('Second')
