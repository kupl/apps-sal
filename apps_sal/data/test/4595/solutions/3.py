s = input()
st = en = 0
for i in range(len(s)):
    if s[i] == "A":
        st = i
        break
for i in range(1,len(s)):
    if s[-i] == "Z":
        en = len(s) - i + 1
        break
print(en-st)
