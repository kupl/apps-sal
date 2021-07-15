n,t = input().split(' ')
s = input()
s = list(s)
t = int(t)
n = int(n)
while t>0 :
    i = 0
    while i<n-1 :
        if s[i]=='B' :
            if s[i+1]=='G' :
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp
                i += 1
        i += 1
    t -= 1
print(''.join(s))

