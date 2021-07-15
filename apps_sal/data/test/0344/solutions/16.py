s = input()
gl = ['a', 'o', 'u', 'i', 'e']
for i in range(len(s)-1):
    if (s[i] not in gl) and (s[i] != 'n'):
        if s[i+1] not in gl:
            print("NO")
            break
else:
    if (s[len(s)-1] not in gl) and (s[len(s)-1] != 'n'):
        print("NO")
    else:
        print("YES")

