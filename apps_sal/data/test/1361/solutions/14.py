# A

n = int(input())
l = input().split()
ans = 10**50
for i in range(n):
    l[i] = int(l[i])
for i in range(1,n-1):
    curr = 0
    m = l[:i]+l[i+1:]
    for i in range(n-2):
        curr = max(curr,m[i+1]-m[i])
    if curr < ans:
        ans = curr
print(ans)

