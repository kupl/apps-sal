eggs=int(input())
diff=0
c=['A' for i in range(eggs)]
for i in range(eggs):
    a=int(input().split()[0])

    if a+diff<501:
        diff+=a
    else:
        c[i]='G'
        
        diff-=1000-a
print(''.join(c))

