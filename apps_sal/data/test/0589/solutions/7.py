s = input()
ans = 1
x = 0
z = 'ABCDEFGHIJ'
L = {}
for item in z:
    L[item] = False
n = len(s)
for i in range(n):
    if s[i] in 'ABCDEFGHIJ' and i == 0:
        ans *= 9
        x += 1
        L[s[i]] = True
    elif s[i] in 'ABCDEFGHIJ' and (not L[s[i]]):
        ans *= 10 - x
        x += 1
        L[s[i]] = True
    elif s[i] == '?' and i == 0:
        ans *= 9
    elif s[i] == '?':
        ans *= 10
print(ans)
