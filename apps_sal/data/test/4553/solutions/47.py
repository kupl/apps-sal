a,b = map(int,input().split())
s = str(input())

if len(s)== a+b+1 \
    and s[a:a+1] =='-' \
    and str.isdecimal(s[0:a]) \
    and str.isdecimal(s[a+1:a+1+b]):
    print('Yes')
else:
    print('No')
