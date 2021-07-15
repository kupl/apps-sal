n=int(input())
s=input()
ans=0
while("RR" in s or "BB" in s or "GG" in s):
    if("RR" in s):
        ans+=s.count("RR")
        s=s.replace("RR","R")
    if("BB" in s):
        ans+=s.count("BB")
        s=s.replace("BB","B")
    if("GG" in s):
        ans+=s.count("GG")
        s=s.replace("GG","G")
print(ans)

