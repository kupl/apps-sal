s = input()
bool = True
for i in range(len(s) - 1):
    for j in range(i + 1,len(s)):
        if s[i] == s[j]:
            bool = False
if bool:
    print('yes')
else:
    print('no')
