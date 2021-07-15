s = input()
t = input()
ans = list(s)

if len(s)>=len(t):
    for i in reversed(list(range(len(s)-len(t)+1))):
        flg=True
        for j in range(len(t)):
            if s[i+j]=="?":
                continue
            if s[i+j]!=t[j]:
                flg=False
                break
        if flg:
            for j in range(len(t)):
                ans[i+j]=t[j]

            break
else:
    flg=False

ans = "".join(ans)
ans = ans.replace("?","a")

print((ans if flg else "UNRESTORABLE"))


