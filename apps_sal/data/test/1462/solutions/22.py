n,k = map(int,input().split())
s=input().lower()
ans=0
letters=[0 for i in range(ord('z')+1)]
for c in s:
    letters[ord(c)]+=1
while k>0:
    ans+=min(k,max(letters))**2
    k-=max(letters)
    letters[letters.index(max(letters))]=0
print(ans)
