s = input()
L = []
temp = 0
for i in range(0, len(s)):
    if s[i] == 'a':
        temp += 1
    elif s[i] == 'b':
        if temp > 0:
            L.append(temp)
            temp = 0
if temp > 0:
    L.append(temp)

ans = 1
for i in L:
    ans = (ans * (i + 1)) % (1000000007)

print((ans - 1) % (1000000007))
