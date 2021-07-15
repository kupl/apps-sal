s = str(input())


a, b = 0, 0

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        a, b = i+1, i+2
        break
    elif i < len(s)-2:
        if s[i] == s[i+2]:
            a, b = i+1, i+3
            break
        
if a == 0:
    print(-1, -1)
else:
    print(a, b)
