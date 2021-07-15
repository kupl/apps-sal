q = int(input())
for j in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    if n == 1:
        if a[0] == a[1] and a[2] == a[3]:
            print('YES')
        else:
            print('NO')
    else:
        b = []
        for i in range(0, 4 * n - 1, 2):
            if a[i] == a[i + 1]:
                b.append(a[i])
        #print(b)
        if len(b) == 2 * n:
            x = b[0] * b[2 * n - 1]
            for i in range(1, n):
                #print(x)
                if b[i] * b[2 * n - i - 1]== x:
                    x = b[i] * b[2 * n - i - 1]
                else:
                    x = 0
                    break
            if x != 0:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
            

