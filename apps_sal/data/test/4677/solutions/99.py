s = input()
res = ""
for i in range(len(s)):
    if s[i] == "1" or s[i] == "0":
        res += s[i]
    elif s[i] == "B" and len(res) != 0:
        res = res[:-1]

print(res)
