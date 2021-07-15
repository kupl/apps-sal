import sys
n,a,b,c = map(int, input().split())
 
s = list()
for i in range(n):
    s.append(input())
 
r = list()
 
for i in range(n):
    if s[i]=='AB':
        if a>b:
            r.append('B')
            a=a-1
            b=b+1
        elif a<b:
            r.append('A')
            a=a+1
            b=b-1
        else:
            if i==n-1 or 'A' in s[i+1]:
                r.append('A')
                a=a+1
                b=b-1
            else: 
                r.append('B')
                a=a-1
                b=b+1
    elif s[i]=='AC':
        if a>c:
            r.append('C')
            a=a-1
            c=c+1
        elif a<c:
            r.append('A')
            a=a+1
            c=c-1
        else:
            if i==n-1 or 'A' in s[i+1]:
                r.append('A')
                a=a+1
                c=c-1
            else: 
                r.append('C')
                a=a-1
                c=c+1
    else:
        if b>c:
            r.append('C')
            b=b-1
            c=c+1
        elif b<c:
            r.append('B')
            b=b+1
            c=c-1
        else:
            if i==n-1 or 'B' in s[i+1]:
                r.append('B')
                b=b+1
                c=c-1
            else: 
                r.append('C')
                b=b-1
                c=c+1
    if min(a,b,c)<0:
        print('No')
        return
 
 
print('Yes')
for str in r:
    print(str)
