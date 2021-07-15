import sys
input = lambda: sys.stdin.readline().strip()
print = lambda s: sys.stdout.write(s)

t = int(input())
for i in range(t):
    n = int(input())
    ls1 = list(map(int, input().split()))
    m = int(input())
    ls2 = []
    for i in range(m):
        ls2.append(tuple(map(int, input().split())))
    if max(ls1)>max(i[0] for i in ls2):
        print('-1\n')
    else:
        temp = {}
        for i in range(1, n+1):
            temp[i] = 0
        for i in ls2:
            try:
                temp[i[1]] = max(temp[i[1]], i[0])
            except:
                temp[i[1]] = i[0]
        d = {}
        d[n] = temp[n]
        for k in range(n-1, 0, -1):
            d[k] = max(d[k+1], temp[k])
        i = 0
        cnt = 1
        ans = 1
        M = ls1[0]
        while True:
            if d[cnt]>=M:
                cnt+=1
                i+=1
                if i==n:
                    break
                M = max(M, ls1[i])
            else:
                ans+=1
                cnt = 1
                M = ls1[i]
        print(str(ans)+'\n')

