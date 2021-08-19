for _ in range(int(input())):
    s = input()
    a = [3] * 26
    i = 0
    while i < len(s):
        j = i
        t = 0
        while j < len(s) and s[j] == s[i]:
            j += 1
            t += 1
        if t & 1:
            a[ord(s[i]) - ord('a')] = min(0, a[ord(s[i]) - ord('a')])
        else:
            a[ord(s[i]) - ord('a')] = min(1, a[ord(s[i]) - ord('a')])
        i = j
    s = ''
    for i in range(26):
        if a[i] == 0:
            s += chr(97 + i)
    print(s)
