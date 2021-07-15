import collections
w = list(input())

cnt = collections.Counter(w)
ans = "Yes"
for v in cnt.values():
    if v%2!=0:
        ans = "No"
        break
        
print(ans)
