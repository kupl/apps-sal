t = int(input())
for i in range(t):
    n =int(input())
    s=input()
    if s[0] == '>' or s[-1]=='<':
        print(0)
    else:
        q=0
        w=0
        for j in s:
            if j=='<':
                q+=1
            else:
                break
        for j in range(len(s)-1, -1, -1):
            if s[j]=='>':
                w+=1
            else:
                break
        print(min(q, w))

