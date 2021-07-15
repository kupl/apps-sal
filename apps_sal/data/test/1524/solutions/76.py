def f(r,l):
    # 3,2
    tmp = [0 for i in range(r+l)]
    if (r+l)%2==0:
        tmp[r-1]=(r+l)//2
        tmp[r]=(r+l)//2
    else:
        if r%2==0:
            tmp[r-1]=(r+l)//2
            tmp[r]=(r+l)//2+1
        else:
            tmp[r-1]=(r+l)//2+1
            tmp[r]=(r+l)//2
    return tmp

s = str(input())
cnt_r = 1
cnt_l = 0
pre = s[0]
ans = []
for i in range(1,len(s)):
    if pre == s[i]:
        if s[i]=='R':
            cnt_r += 1
        else:
            cnt_l += 1
    else:
        if s[i]=='R':
            ans += f(cnt_r,cnt_l)
            pre = s[i]
            cnt_r = 1
            cnt_l = 0
        else:
            pre = s[i]
            cnt_l += 1
ans += f(cnt_r,cnt_l)

tmp = ''
for i in ans:
    tmp += str(i) + ' '
print(tmp[:-1])
