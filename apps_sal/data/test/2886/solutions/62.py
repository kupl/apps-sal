s = input()
left = -1;right = -1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        left = i+1;right=i+2
        break
    if not i == len(s)-2:
        if s[i]==s[i+2]:
            left = i+1;right=i+3
            break
print(left, right)
