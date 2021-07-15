n,k = map(int,input().split())
s = input()
chars = {}
for c in s:
    chars[c]=1
s += '\0'
ans = 0
for c in chars:
    nowl = 0
    a = 0
    for d in s:
        if d == c:
            nowl+=1
        elif nowl>0:
            a += nowl//k
            nowl = 0
    ans = max(ans,a)
print(ans)
