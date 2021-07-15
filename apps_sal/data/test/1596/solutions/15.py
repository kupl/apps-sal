s = input()
L = [0] * (len(s) + 1)
inf = 1000000007
L[0] = 1
L[1] = 1
for i in range(1, len(s)):
    if s[i] == 'm' or s[i] == 'w':
        break
    if s[i] == 'u':
        if s[i - 1] == 'u':
            L[i + 1] = (L[i] + L[i - 1]) % inf
        else:
            L[i + 1] = L[i]
    elif s[i] == 'n':
        if s[i - 1] == 'n':
            L[i + 1] = (L[i] + L[i - 1]) % inf
        else:
            L[i + 1] = L[i]
    else:
        L[i + 1] = L[i]
if s[0] == 'm' or s[0] == 'w':
        L[len(s)] = 0
print(L[len(s)])
    
    
    
        

