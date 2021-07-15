s = input()
if s[0] != 'a':
    print("NO")
else:
    maxs = s[0]
    for i in range(1, len(s)):
        if ord(s[i]) - ord(maxs) > 1:
            print("NO")
            break
        if ord(s[i]) > ord(maxs):
            maxs = s[i]        
    else:
        print("YES")

