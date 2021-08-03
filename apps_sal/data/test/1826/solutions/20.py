n = int(input())
s = input()
i = 0
while i + 1 < len(s):
    if s[i] == "U" and s[i + 1] == "R" or s[i] == "R" and s[i + 1] == "U":
        s = s[:i] + s[i + 2:]
    else:
        i += 1
print(len(s) + (n - len(s)) // 2)
