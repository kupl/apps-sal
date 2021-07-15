#template
def inputlist(): return [int(j) for j in input().split()]
#template
n,k = inputlist()
s = input()
s = s+s
n*=2

def returnWinner(a,b):
    if a == b:
        return a
    else:
        if a+b == "RS" or a+b == "SR":
            return "R"
        if a+b == "RP" or a+b == "PR":
            return "P"
        if a+b == "PS" or a+b == "SP":
            return "S"

if k == 1:
    ans = returnWinner(s[0],s[1])
    print(ans)
    return
from copy import deepcopy
for i in range(k-1):
    s = s+s
    t = ["R"]*min(len(s)//2,2**(k-1-i))
    for j in range(0,min(len(s),2**(k-i)),2):
        t[j//2] = returnWinner(s[j],s[j+1])
    s = deepcopy(t)
    if len(s) == 1:
        print(s[0])
        return


print(s[0])
