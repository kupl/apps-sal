def jikan(now_t,i):
    if i==n:
        return now_t
    else:
        if now_t<=s[i]:
            now_t = s[i]
        else:
            tmp1 = now_t//f[i]
            if now_t%f[i]!=0:
                now_t = (tmp1+1)*f[i]
        tmp = jikan(now_t+c[i],i+1)
        return tmp

n = int(input())
c,s,f = [0],[0],[0]
for i in range(n-1):
    ci,si,fi = list(map(int,input().split()))
    c.append(ci)
    s.append(si)
    f.append(fi)
#print(c,s,f)
for i in range(1,n+1):
    print((jikan(0,i)))

