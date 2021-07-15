n, m, q = list(map(int, input().split()))
a = [[]]
for i in range(n):
    a.append([0] + list(map(int, input().split())))
x, y = list(map(int, input().split()))
a[x][y] = (a[x][y] + 1) % 2
ma = 0
curr = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] == 0:
            ma = max(curr, ma)
            curr = 0
        else:
            curr += 1
    ma = max(ma, curr)
    curr = 0
res = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] == 0:
            if curr == ma: res += 1
            curr = 0
        else:
            curr += 1
    if curr == ma: res += 1
    curr = 0
print(ma)
for i in range(q - 1):
    x, y = list(map(int, input().split()))
    if a[x][y] == 1:
        j = y - 1
        here = 1
        while j >= 0 and a[x][j] == 1:
            j -= 1
            here += 1
        j = y + 1
        while j <= m and a[x][j] == 1:
            j += 1
            here += 1
        a[x][y] = 0
        if here == ma: res -=1
        if res >= 1: print(ma)
        else:
            ma = 0
            curr = 0
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if a[i][j] == 0:
                        ma = max(curr, ma)
                        curr = 0
                    else:
                        curr += 1
                ma = max(ma, curr)
                curr = 0
            res = 0
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if a[i][j] == 0:
                        if curr == ma: res += 1
                        curr = 0
                    else:
                        curr += 1
                if curr == ma: res += 1
                curr = 0
            print(ma)       
    else:
        a[x][y] = 1
        j = y - 1
        here = 1
        while j >= 0 and a[x][j] == 1:
            j -= 1
            here += 1
        j = y + 1
        while j <= m and a[x][j] == 1:
            j += 1
            here += 1      
        if here > ma:
            ma = here
            res = 1
        elif here == ma:
            res += 1
        print(ma)
        
        

