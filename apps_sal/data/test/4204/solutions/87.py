s = input()
k = int(input()) - 1
for i in range(len(s)):
    if s[i] != '1' or i == k:
        break
print(s[i])
