s = input()
ans = ["",""]
for i in range(len(s)):
    if s[i] == "A" and ans[0] == "":
        ans[0] = i+1
    if ans[0] != "" and s[i]=="Z":
        ans[1] = i+1
print(ans[1]-ans[0]+1)
