s = input()
n = len(s)
ans = (n+1)//2
if n%2:
    x = s[n//2]
    for i in range(1,n//2+1):
        if s[n//2-i] == s[n//2+i] == x:
            ans += 1
        else:
            break
if n%2==0:
    if s[n//2] == s[n//2-1]:
        ans += 1
        x = s[n//2]
        for i in range(1,n//2):
            if s[n//2-1-i] == s[n//2+i] == x:
                ans += 1
            else:
                break
print(ans)
