for _ in range (int(input())):
    s=input()
    a = []
    flag = 0
    count = 0
    for i in range (len(s)):
        if s[i]=='1':
            count+=1
        else:
            a.append(count)
            count=0
        if i==len(s)-1 and count!=0:
            a.append(count)
    a.sort(reverse=True)
    ans = 0
    for i in range(len(a)):
        if i%2==0:
            ans+=a[i]
    print(ans)
