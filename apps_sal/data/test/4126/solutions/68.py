s = input()
n = len(s)

s1 = s[0:(n - 1) // 2]
s2 = s[(n + 1) // 2:n]

s_reverse = s[::-1]
s1_reverse = s1[::-1]
s2_reverse = s2[::-1]

if s == s_reverse and s1 == s1_reverse and s2 == s2_reverse:
    print("Yes")
else:
    print("No")
