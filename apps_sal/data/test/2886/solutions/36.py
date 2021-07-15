s = input()
l = len(s)
for i in range(1,l):
    if s[i] == s[i-1]:
        print(i,i+1)
        break
else:
    for i in range(2,l):
        if s[i] == s[i-2]:
            print(i-1,i+1)
            break
    else:
        print(-1,-1)
