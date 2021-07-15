s = list(input())
n = len(s)
s1 = s[0:(n-1)//2]
s2 = s[(n-1)//2+1:n]
sr = list(reversed(s))
s1r = list(reversed(s1))
s2r = list(reversed(s2))

if s == sr and s1 == s1r and s2 == s2r:
    print("Yes")
    return

print("No")
