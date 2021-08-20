mp = [8, -1, -1, 3, 6, 9, 4, 7, 0, 5]
str = input()
for i in range(len(str)):
    if ord(str[i]) - ord('0') != mp[ord(str[len(str) - 1 - i]) - ord('0')]:
        exit(print('No'))
print('Yes')
