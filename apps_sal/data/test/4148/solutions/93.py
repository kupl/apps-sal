n = int(input())
s = input()
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_s = ""
for i in range(len(s)):
    for j in range(26):
        if s[i] == alp[j]:
            if j + n >= 26:
                new_s += alp[j + n - 26]
            else:
                new_s += alp[j + n]
print(new_s)
