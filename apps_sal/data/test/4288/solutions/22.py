s = input().split()
if (s[0] == s[1] and s[1] != s[2]) or (s[0] != s[1] and s[1] == s[2]) or (s[0] == s[2] and s[1] != s[2]):
    print("Yes")
else:
    print("No")
