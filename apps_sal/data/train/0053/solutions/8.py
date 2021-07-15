Q = int(input())


total = []
for _ in range(Q):
    n, s = input().split()
    n=int(n)

    seq = []
    curlen = 1
    for i in range(len(s)):
        if s[i]=='<':
            curlen+=1
        else:
            seq.append(curlen)
            curlen=1
    seq.append(curlen)
    curr = n
    ans =[]
    for sq in seq:
        ans.extend(range(curr-sq+1,curr+1))
        curr-=sq
    total.append(' '.join(map(str,ans)))

    curr = n
    ans = ['']*n
    for i in range(len(s)-1,-1,-1):
        if s[i]=='<':
            ans[i+1]=str(curr)
            curr-=1
    for i in range(n):
        if not ans[i]:
            ans[i]=str(curr)
            curr-=1
    total.append(' '.join(ans))


print(*total, sep='\n')
