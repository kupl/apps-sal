from sys import stdin
"""
n=int(stdin.readline().strip())
n,m=map(int,stdin.readline().strip().split())
s=list(map(int,stdin.readline().strip().split()))
s=stdin.readline().strip()
"""
T = int(stdin.readline().strip())
for caso in range(T):
    n, k = list(map(int, stdin.readline().strip().split()))
    s = list(stdin.readline().strip())
    aux = []
    last = -1
    for i in range(n):
        if i > 0 and s[i] == 'L' and s[i - 1] == 'W':
            last = i
        if i < n - 1 and s[i] == 'L' and s[i + 1] == 'W' and last != -1:
            aux.append([i - last, last, i])
    aux.sort()
    for i in aux:
        for j in range(i[1], i[2] + 1):
            if k > 0:
                s[j] = 'W'
                k -= 1
    ini = -1
    fin = n
    for i in range(n):
        if s[i] == 'W':
            ini = i - 1
            break
    for i in range(n - 1, -1, -1):
        if s[i] == 'W':
            fin = i + 1
            break
    for i in range(ini, -1, -1):
        if k > 0:
            s[i] = 'W'
            k -= 1
    for i in range(fin, n):
        if k > 0:
            s[i] = 'W'
            k -= 1
    ans = 0
    if ini == -1 and fin == n:
        for i in range(n):
            if k > 0:
                s[i] = 'W'
                k -= 1
    for i in range(n):
        if s[i] == 'W':
            if i > 0 and s[i - 1] == 'W':
                ans += 2
            else:
                ans += 1
    print(ans)
