n, m = map(int, input().strip().split())
a    = [int(x) for x in input().strip().split()]
t    = [0 for i in range(0, 101)]
for i in range(0, n):
    c, j, s = a[i], 1, 0
    flag = 0
    while(j < 101):
        cnt = min(t[j], (m-c)//j)
        s += cnt
        c += j*cnt
        if(cnt < t[j]):
            flag = 1
            break
        j+=1
    if(flag == 0):
        print(0, end=' ')
    else:
        print(i-s, end=' ')
    t[a[i]]+=1

