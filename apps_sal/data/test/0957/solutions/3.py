s = input()
a = 0
pat = "heidi"
for i in s:
    if i == pat[a]:
        a+=1
        if(a == 5):
            break
print("YES") if a==5 else print("NO")
