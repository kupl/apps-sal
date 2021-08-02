def TrueCount(a):
    c = 0
    for i in a:
        if(i == True):
            c += 1
    return c


def uniqueStrings(a, s):
    b = []
    c = []
    x = 0
    c.append(s[0])
    for i in range(len(s)):
        if s[i] not in c:
            b.append(s[x:i])
            c.append(s[i])
            x = i
    b.append(s[x:len(s)])
    return b


n = int(input())
s = input()

a = [False] * 26

for i in s:
    a[ord(i) - ord('a')] = True

k = TrueCount(a)

if(k < n):
    print("NO")
else:
    print("YES")
    b = uniqueStrings(a, s)
    i = 0
    while(i < n - 1):
        print(b[i])
        i += 1
    print(''.join(b[i:len(b)]))
