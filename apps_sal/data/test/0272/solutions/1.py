s1 = input()
s2 = input()
used = ['$'] * 256
for i in range(len(s1)):
    c1 = s1[i]
    c2 = s2[i]
    if (c1 == c2):
        if (used[ord(c1)] == '$' or used[ord(c1)] == '%') and (used[ord(c2)] == '$' or used[ord(c2)] == '%'):
            used[ord(c1)] = '%'
            used[ord(c2)] = '%'
        else:
            print(-1)
            return
    else:
        if (used[ord(c1)] == '$' or used[ord(c1)] == c2) and (used[ord(c2)] == '$' or used[ord(c2)] == c1):
            used[ord(c1)] = c2
            used[ord(c2)] = c1
        else:
            print(-1)
            return
ans = []
for i in range(256):
    if (used[i] == '$' or used[i] == '%'):
        continue
    else:
        if ord(used[i]) < i:
            ans.append([used[i], chr(i)])
print(len(ans))
for elem in ans:
    print(elem[0], elem[1])
