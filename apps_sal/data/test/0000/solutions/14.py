s = str(input().strip())
i = 0
n = len(s)
while i < n and s[i] != '[':
    i+=1
if(i == n):
    print(-1)
    return
j = n-1
while j > i and s[j] != ']':
    j-=1
if(j <= i):
    print(-1)
    return
while i < j and s[i] != ':':
    i+=1
if(i == j):
    print(-1)
    return
while j > i and s[j] != ':':
    j-=1
if(j == i):
    print(-1)
    return
k = i+1
c = 0
while k < j:
    if(s[k] == '|'):
        c+=1
    k+=1
print(c+4)

