q = int(input())
for x in range(q):   
    n = int(input())
    s = str(input())
    t = str(input())
    ss = sorted(s)
    tt = sorted(t)
    if ss != tt:
        ans = -1
    else:
        ans = 1000000000
        for i in range(n):
            k = i
            for j in range(n):
                if k < n and s[j] == t[k]:
                    k+=1
                ans = min(ans, n - k + i)
    print(ans)
