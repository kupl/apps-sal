n = int(input())
a = list(map(int,input().split()))

s = [0]*(n+1)
for x in a:
    s[x] += 1
    

p = 0
for i in range(1,n+1):
    if s[i] >= 2:
        p += s[i]*(s[i]-1)//2

for i in range(n):
    ans = p - s[a[i]]*(s[a[i]]-1)//2 + (s[a[i]]-2)*(s[a[i]]-1)//2
    print(ans)
