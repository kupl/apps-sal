s = input()
t = input()
cot = 0
for i in range(len(s)):
    if s[i] == t[i]:
        cot += 1
print(len(s) - cot)
