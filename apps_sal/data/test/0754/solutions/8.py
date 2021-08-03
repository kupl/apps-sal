n = int(input())
s = input()
c = " "
tmp = 0
for i in range(len(s)):
    if s[i] != c:
        tmp += 1
        c = s[i]
print(len(s) - tmp)
