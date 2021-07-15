n = int(input())
v = list(map(int,input().split()))
for i in range(1,(1<<n)-1):
    s1, s2 = 0, 0
    b = 0
    for j in range(n):
        if i & 1<<j:
            s1 += v[j]
            b += 1
        else:
            s2 += v[j]
    if s1 != s2:
        print(b)
        for j in range(n):
            if i & 1<<j:
                print(j+1,end=' ')
        break
else:
    print(-1)

