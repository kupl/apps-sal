s = input()
n = len(s)
dp2, dp3 = [0 for i in range(n)], [0 for i in range(n)]
if(n < 7):
    print(0)
else:
    if n - 2 > 4:
        dp2[n - 2] = 1
    if n - 3 > 4:
        dp3[n - 3] = 1
    # for(i=n-4;i>5;i--)
    i = n - 4
    while i >= 5:
        #print("i=%d"% i)
        dp2[i] = (dp3[i + 2] | (dp2[i + 2] & (s[i:i + 2] != s[i + 2:i + 4])))
        #if s[i:i+2]!=s[i+2:i+4] : t=1
        # else: t=0
        #print("%s  %s" %(s[i:i+2],s[i+2:i+4]))
        dp3[i] = dp2[i + 3] | (dp3[i + 3] & (s[i:i + 3] != s[i + 3:i + 6]))
        # print(s[i:i+3]+s[i+3:i+6])
        i = i - 1
    a = set()
    for i in range(n):
        if dp2[i]:
            a.add(s[i:i + 2])
        if dp3[i]:
            a.add(s[i:i + 3])
    a = sorted(list(a))
    print(len(a))
    for i in a:
        print(i)
