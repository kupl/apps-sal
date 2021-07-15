def ans():
    n, m, k = map(int, input().split())
    a = list([] for i in range(n))
    s = [0]*m
    for i in range(n):
        a[i] = input()
    for i in range(1,n):
        for j in range(m):
            if i < m-j and a[i][j+i] == 'L':
                s[j]+=1
            if i <= j and a[i][j-i] == 'R':
                s[j]+=1
            if i+i < n and a[i+i][j] == 'U':
                s[j]+=1
    print(*s)
ans()
