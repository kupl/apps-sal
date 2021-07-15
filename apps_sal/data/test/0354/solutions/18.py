s=input()
t=input()
glas= ['a', 'e', 'i', 'o' ,'u']
if len(s)==len(t):
    for i in range(len(s)):
        if (s[i] in glas and t[i] in glas) or (s[i] not in glas and t[i] not in glas):
            counter=0
        else:
            print('No')
            break
    else:
        print('Yes')
else:
    print('No')

