n,q = map(int,input().split())
s = input()
ans = []
a = [0]*(10**5+1)
add = 0
check = False
for i in range(n):
    if check and s[i] == 'C':
        add +=1
    if s[i] == 'A':
        check = True
    else:
        check = False
    
    a[i] += add
for i in range(q):
    b,c = map(int,input().split())
    ans.append(a[c-1]-a[b-1])
for i in range(q):
    print(ans[i])
