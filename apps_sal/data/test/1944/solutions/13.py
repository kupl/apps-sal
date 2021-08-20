n = int(input())
if n == 1:
    (a, b) = list(map(int, input().split()))
    print('Poor Alex')
else:
    x = [0] * n
    for i in range(n):
        x[i] = [0] * 2
        (x[i][0], x[i][1]) = list(map(int, input().split()))
    x.sort()
    ans = False
    for i in range(1, n):
        if x[i][1] < x[i - 1][1]:
            ans = True
            break
    if ans == True:
        print('Happy Alex')
    else:
        print('Poor Alex')
