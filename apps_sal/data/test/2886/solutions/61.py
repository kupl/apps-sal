s = input()
n = len(s)
for i in range(n):
    if i+1 < n:
        if s[i] == s[i+1]:
            print(str(i+1)+" "+str(i+1+1))
            return
    if i+2 < n:
        if s[i] == s[i+2]:
            print(str(i+1)+" "+str(i+2+1))
            return
    if i > 0:
        if s[i] == s[i-1]:
            print(str(i)+" "+str(i+1))
            return
    if i > 1:
        if s[i] == s[i-2]:
            print(str(i-1)+" "+str(i+1))
            return
print("-1 -1")
return
