n, m = map(int, input().split())
our = [input() for i in range(n)]
first = -1
for i in range(n):
    if 'B' in our[i]:
        first = i
        break
last = -1
for i in range(n- 1, -1, -1):
    if 'B' in our[i]:
        last = i
        break  
if first == -1:
    print(1)
else:
    f2 = -1
    l2 = -1
    for i in range(m):
        a = [our[j][i] for j in range(n)]
        if 'B' in a:
            f2 = i
            break
    for i in range(m - 1, -1, -1):
        a = [our[j][i] for j in range(n)]
        if 'B' in a:
            l2 = i
            break    
    if last - first + 1 > m or l2 - f2 + 1 > n:
        print(-1)
    else:
        res = 0
        for i in range(first, last + 1):
            for j in range(f2, l2 + 1):
                if our[i][j] == 'W':
                    res += 1
        res += max(last - first + 1, l2 - f2 + 1) ** 2 - (last - first + 1) * (l2 - f2 + 1)
        print(res)
