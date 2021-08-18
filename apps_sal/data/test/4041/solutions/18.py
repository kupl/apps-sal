def is_subseq(s, t):
    if(len(t) > len(s)):
        return False
    i = 0
    j = 0
    while(j < len(t)):
        if(s[i] == t[j]):
            i += 1
            j += 1
        else:
            i += 1
        if(i == len(s)):
            break
    return j == len(t)


s = input()
t = input()
mx = 0
for i in range(len(s)):
    for j in range(len(s)):
        l = min(i, j)
        r = max(i, j)
        s2 = s[:l] + s[r:]
        if(is_subseq(s2, t) == True):
            mx = max(mx, r - l)
for i in range(len(s)):
    s2 = s[:i]
    if(is_subseq(s2, t) == True):
        mx = max(mx, len(s) - i)
    s2 = s[i:]
    if(is_subseq(s2, t) == True):
        mx = max(mx, i)

print(mx)
