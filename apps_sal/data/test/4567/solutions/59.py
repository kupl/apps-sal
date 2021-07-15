n = int(input())
s = [int(input()) for i in range(n)]
s.sort()
ans = sum(s)

if ans%10==0:
    for i in range(len(s)):
        if s[i]%10!=0 :
            ans -= s[i]
            break
    else:
        ans = 0

print(ans)

