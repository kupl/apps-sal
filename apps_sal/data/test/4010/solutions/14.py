def solve():
    n = int(input())
    a = list(map(int, input().split()))
    i1 = 0
    i2 = n
    flag = False
    for i in range(n-2):
        e1 = a[i]
        for j in range(i+2, n):
            if e1 == a[j]:
                print('YES')
                flag = True
                break
        if flag == True:
            break
    if flag == False:
        print('NO')

for i in range(int(input())):
    solve()
