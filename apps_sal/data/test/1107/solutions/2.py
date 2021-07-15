n = int(input())
s = input().strip()
pl = 0
ans = 0
for q in range(len(s)):
    if q>=3 and pl==0:
        if s[q-3]==s[q-2]==s[q-1]:
            ans+=1
    pl = (pl+1) % n 
print(ans)
