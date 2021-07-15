n = int(input())
s = input()
types = len(set(s))
d = dict()
c = 0
j = 0
ans = 10**10
for i in range(n):
    if s[i] not in d:
        d[s[i]] = 0
        c+=1
    d[s[i]]+=1
    if c ==types:
        while d[s[j]] > 1:
            d[s[j]]-=1
            j+=1
        ans = min(ans,i-j+1)
print(ans)

