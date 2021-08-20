n = int(input())
mn = set('qwertyuiopasdfghjklzxcvbnm')
f = False
k = 0
for i in range(n):
    s = input().split()
    if f:
        if s[0] == '?' and set(s[1]) != mn or s[0] == '!':
            k += 1
        continue
    if s[0] == '?' and i != n - 1:
        mn -= set(s[1])
    elif s[0] == '!':
        mn &= set(s[1])
    elif s[0] == '.':
        mn -= set(s[1])
    if len(mn) == 1:
        f = True
print(k)
