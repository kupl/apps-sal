def solve(s,n,w):
    if s==w:
        return "YES"
    for i in range(n):
        for j in range(i,n,1):
            ns=s[0:i]+s[j+1:]
            if len(ns) != len(w):
                continue
            for k in range(len(ns)):
                if ns[k] != w[k]:
                    break
            else:
                return "YES"
    return "NO"

s=input()
n=len(s)
w="CODEFORCES"
print(solve(s,n,w))

