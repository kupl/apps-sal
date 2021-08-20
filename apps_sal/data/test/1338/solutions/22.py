(n, m) = map(int, input().split())
s = 0
flag = False
k = 0
myset = set()
flag1 = True
for j in range(n):
    if n in myset:
        for i in range(n, 0, -1):
            if i not in myset:
                print(i, end=' ')
                flag1 = False
    if flag1 == False:
        break
    flag = False
    s = 0
    for i in range(n):
        if s < m <= s + 2 ** (n - i - 2 - k):
            print(i + 1 + k, end=' ')
            myset.add(i + 1 + k)
            k = i + 1 + k
            flag = True
            break
        s += 2 ** (n - i - 2 - k)
    if flag == False:
        print(n, end=' ')
        myset.add(n)
        k = n
    m -= s
