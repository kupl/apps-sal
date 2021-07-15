s = input()
n = len(s)
L = list(s)
S = 'abcdefghijklmnopqrstuvwxyz'
ind = 0
for i in range(n):
    if (ind < 26 and s[i] <= S[ind]):
        L[i] = S[ind]
        ind += 1
        

    
ans = ""
for item in L:
    ans += item

if (ind >= 26):
    print(ans)
else:
    print(-1)
    

