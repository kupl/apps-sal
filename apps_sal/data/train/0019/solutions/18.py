for i in range(int(input())):
    n,k,d = map(int,input().split())
    a = [int(s) for s in input().split()]
    s = dict()
    for j in range(d):
        if s.get(a[j],0) == 0:
            s[a[j]] = 1
        else:
            s[a[j]] += 1
    m = len(s)   
    for j in range(1,n-d+1):
        if s[a[j-1]] == 1:
            s.pop(a[j-1])
        else:
            s[a[j-1]] -= 1
        if s.get(a[j+d-1],0) == 0:
            s[a[j+d-1]] = 1
        else:
            s[a[j+d-1]] += 1
        if len(s) < m:
            m = len(s)
    print(m)
