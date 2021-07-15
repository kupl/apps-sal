s=input()
ans="Yes"
for i in range(4):
    if s.count(s[i])!=2:
        ans="No"
print(ans)
