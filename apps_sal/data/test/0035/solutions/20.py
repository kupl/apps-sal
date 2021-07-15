n, m = list(map(int, input().split()))
fl = [input() for i in range(n)]
c1 = fl[0][0]
BOOL = False
for i in range(n):
    if fl[i][0] != c1:
        BOOL = True
        break
if BOOL:
    BOOL = False 
    if n % 3 == 0:
        for i in range(n // 3)[:n//3]:
            for j in range(m):
                if fl[i][j] != c1:
                    BOOL = True
        c2 = fl[n//3][0]
        if not BOOL:
            for i in range(n)[n//3:-(n//3)]:
                for j in range(m):
                    if fl[i][j] != c2:
                        BOOL = True
        c3 = fl[-(n//3)][0]
        if not BOOL:
            for i in range(n)[-(n//3):]:
                for j in range(m):
                    if fl[i][j] != c3:
                        BOOL = True
        if c1 == c2 or c2 == c3 or c1 == c3:
            print('NO')
        else:
            if  BOOL:
                print('NO')
            else:
                print('YES')
    else:
        print('NO')
else:
    if m % 3 == 0:
        for i in range(m)[:m//3]:
            for j in range(n):
                if fl[j][i] != c1:
                    BOOL = True
        c2 = fl[0][m//3]
        if not BOOL:
            for i in range(m)[m//3:-(m//3)]:
                for j in range(n):
                    if fl[j][i] != c2:
                        BOOL = True
        c3 = fl[0][-(m//3)]
        if not BOOL:
            for i in range(m)[-(m//3):]:
                for j in range(n):
                    if fl[j][i] != c3:
                        BOOL = True
        if c1 == c2 or c2 == c3 or c1 == c3:
            print('NO')
        else:
            if  BOOL:
                print('NO')
            else:
                print('YES')
    else:
        print('NO')

