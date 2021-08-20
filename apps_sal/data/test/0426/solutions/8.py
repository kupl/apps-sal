a = list(map(int, input().split()))
n = a[0]
k = a[1]
s = input()
s1 = ''
changed = 0
for i in range(len(s)):
    if changed >= k:
        for j in range(i, len(s)):
            s1 += s[j]
        break
    if i == 0 and i < len(s) - 1:
        if s[i] != '1':
            s1 += '1'
            changed += 1
        else:
            s1 += s[i]
    elif s[i] != '0':
        s1 += '0'
        changed += 1
    else:
        s1 += s[i]
print(s1)
