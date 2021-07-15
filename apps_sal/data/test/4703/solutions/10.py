S = input()
n = len(S)
 
ans = 0
 
for i in range(2**(n-1)):
    t = S[0]
    for j in range(n-1):
        if (i>>j)&1:
            t += "+"
        t += S[j+1]
    ans += eval(t)
 
print(ans)
