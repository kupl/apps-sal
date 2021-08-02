s = input()
i = s.index("A")
j = len(s) - s[::-1].index("Z")
print(len(s[i:j]))
