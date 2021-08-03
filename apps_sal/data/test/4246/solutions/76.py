s = input()
t = input()

res = 0

for i in range(len(s)):
    if s[i] == t[i]:
        res += 1

print(res)
