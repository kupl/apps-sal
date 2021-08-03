n = int(input())
s = input()
lst = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ans = ''
for i in range(len(s)):
    ans += lst[(lst.index(s[i]) + n) % 26]

print(ans)
