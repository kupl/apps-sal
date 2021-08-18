m, n = input().strip().split(' ')
m, n = int(m), int(n)
arr = list(map(int, input().strip().split(' ')))
days = 0
if(m > n):
    print(0)
else:
    mp = {}
    for i in arr:
        if(i in mp):
            mp[i] += 1
        else:
            mp[i] = 1
    temp = []
    for i in mp:
        temp.append(mp[i])
    temp.sort()
    days = 0
    j = 1
    while(1):
        cnt = 0
        for i in temp:
            cnt += i // j
            if(cnt >= m):
                break
        if(cnt < m):
            break
        days += 1
        j += 1
    print(days)
