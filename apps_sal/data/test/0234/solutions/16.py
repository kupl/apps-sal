n, m = list(map(int, input().split()))
a = []
for _ in range(n):
    a.append(list(map(str, input().strip())))
# print(a)
k = 0
for i in range(n):
    for j in range(m):
        p = a[i][j]
        # print(p)
        if p == '.':
            if i - 1 >= 0:
                if j - 1 >= 0 and a[i - 1][j - 1] == '*':
                    k = 1
                if j + 1 < m and a[i - 1][j + 1] == '*':
                    k = 1
                if a[i - 1][j] == '*':
                    k = 1
            if j - 1 >= 0 and a[i][j - 1] == '*':
                k = 1
            if j + 1 < m and a[i][j + 1] == '*':
                k = 1
            if i + 1 < n:
                if j - 1 >= 0 and a[i + 1][j - 1] == '*':
                    k = 1
                if j + 1 < m and a[i + 1][j + 1] == '*':
                    k = 1
                if a[i + 1][j] == '*':
                    k = 1
        if ord(p) >= ord('1') and ord(p) <= ord('8'):
            x = ord(p) - ord('0')
            c = 0
            if i - 1 >= 0:
                if j - 1 >= 0 and a[i - 1][j - 1] == '*':
                    c += 1
                if j + 1 < m and a[i - 1][j + 1] == '*':
                    c += 1
                if a[i - 1][j] == '*':
                    c += 1
            if j - 1 >= 0 and a[i][j - 1] == '*':
                c += 1
            if j + 1 < m and a[i][j + 1] == '*':
                c += 1
            if i + 1 < n:
                if j - 1 >= 0 and a[i + 1][j - 1] == '*':
                    c += 1
                if j + 1 < m and a[i + 1][j + 1] == '*':
                    c += 1
                if a[i + 1][j] == '*':
                    c += 1
            if c != x:
                k = 1
            #print("c=%d x=%d" %(c,x))
        if k == 1:
            break
    if k == 1:
        break
if k == 0:
    print("YES")
else:
    print("NO")
