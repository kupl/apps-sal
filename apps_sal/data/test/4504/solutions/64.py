s = list(input())
ans = 0
if len(s)%2==0:
    s = s[:-2]
else:
    s.pop(-1)

while len(s)>0:
    if s[0:int(len(s)/2)]==s[int(len(s)/2):len(s)]:
        ans = len(s)
        break
    else:
        s = s[:-2]
        
print(ans)
