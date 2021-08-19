n = int(input())
s = input()
if len(s) % 2 == 1:
    print('No')
elif s[:len(s) // 2] == s[len(s) // 2:]:
    print('Yes')
else:
    print('No')
