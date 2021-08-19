s = input()
flag = [0] * 26
for i in range(len(s)):
    flag[ord(s[i]) - 97] += 1
res = 'Yes'
for i in range(26):
    if flag[i] % 2 == 1:
        res = 'No'
print(res)
