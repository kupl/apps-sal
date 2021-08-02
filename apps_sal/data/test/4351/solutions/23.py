s = input()
n = len(s) // 2

flg = True
for i in range(n):
    if s[i] != s[-i - 1]:
        flg = False
        break

print('Yes') if flg else print('No')
