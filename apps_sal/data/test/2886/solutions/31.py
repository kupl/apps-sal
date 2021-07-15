s = input()
l = len(s)
s += "!"*10
for i in range(l):
    tar = s[i]
    for j in range(i+1,i+3):
        if s[i] == s[j]:
            print(i+1,j+1)
            return
print(-1,-1)
