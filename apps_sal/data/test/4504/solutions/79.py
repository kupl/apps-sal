S = input()
s = S
for i in range(len(S)):
    s = s[:-1]
    if s[:len(s)//2] == s[len(s)//2:]:
        print(len(s))
        return
