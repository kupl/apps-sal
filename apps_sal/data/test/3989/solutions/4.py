S='1689'
s=input()
Z=s.count('0')
s=s.replace('0','')
for i in S:t=s.index(i);s=s[:t]+s[t+1:]
k=0
for i in s:k=(k*10+ord(i)-ord('0'))%7
for a in S:
    for b in S:
        for c in S:
            for d in S:
                if len(set(a+b+c+d))==4 and (k*10000+int(a+b+c+d))%7==0:
                    print(s+a+b+c+d+'0'*Z)
                    return
