def solve(s,t):
    ss=s.split('*')
    if len(ss)==1:
        return ss[0]==t
    else:
        return t.startswith(ss[0]) and t.endswith(ss[1]) and len(t)>=len(s)-1

input()
s=input()
t=input()
if solve(s,t):
    print("YES")
else:
    print("NO")
