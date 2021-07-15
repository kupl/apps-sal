s = input()

s_ = s[0]

for c in s:
    if s_[-1]!=c:
        s_ += c
print(len(s_)-1)
