s = list(input())

count = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1] and s[i] == "0":
        s[i + 1] = "1"
        count += 1
    elif s[i] == s[i + 1] and s[i] == "1":
        s[i + 1] = "0"
        count += 1
    else:
        pass

print(count)
