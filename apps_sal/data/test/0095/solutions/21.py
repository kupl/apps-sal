def check(lst):
    b = True
    sost = 0
    for i in range(1, len(a)):
        if lst[i] > lst[i - 1]:
            if sost != 0:
                b = False
                break
            sost = 0
        elif lst[i] == lst[i - 1]:
            if sost == 2:
                b = False
                break
            sost = 1
        else: 
            sost = 2
    return b
n = int(input())
a = list(map(int, input().split()))
if check(a):
    print('YES')
else:
    print('NO')

