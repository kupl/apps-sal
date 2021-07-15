n = int(input())
s = bin(n)[2:]
rem = 6-len(s)
s="0"*rem+s
ans = [0]*6
ans[0]=s[0]
ans[1]=s[5]
ans[2]=s[3]
ans[3]=s[2]
ans[4]=s[4]
ans[5]=s[1]
an = "".join(ans)
print(int(an,2))
