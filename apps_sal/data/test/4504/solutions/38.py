s = input()
res = 0

for i in range(len(s)):
    if i % 2 != 0:
        pass
    else:
        if s[:i // 2] == s[i // 2:i]:
            res = i
print(res)
