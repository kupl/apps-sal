s = input()
x = []
for i in range(len(s)):
    if s[i] == "0":
        x.append("0")
    elif s[i] == "1":
        x.append("1")
    elif s[i] == "B" and len(x) > 0:
        x.pop(-1)
print("".join(x))
