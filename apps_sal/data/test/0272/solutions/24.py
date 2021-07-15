s = input()
t = input()
A = dict()
ans = set()
per  =0
for j in range(len(s)):
    if s[j] in A and t[j] in A:
        if A[s[j]] != t[j] or A[t[j]] != s[j]:
            per = 1
            break
        
            
    elif t[j] in A and s[j] not in A:
        per=1
        break
    elif s[j] in A and t[j] not in A:
        per=1
        break
    else:
        A[s[j]] = t[j]
        A[t[j]] = s[j]
        if s[j] != t[j]:
            if s[j]+t[j] not in ans and t[j]+s[j] not in ans:
                ans.add(s[j]+t[j])
if per != 1:
    print(len(ans))
    for j in ans:
        print(j[0], j[1])
else:
    print(-1)
