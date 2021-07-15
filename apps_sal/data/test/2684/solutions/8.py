n = int(input())
s = input()

if s == s[::-1]:
    print(len(s))
    print(s)
else:
    out = ''
    maxLen = 0
    for i in range(n):
        for j in range(n):
            cur = s[i: i + j]
            if cur != out and len(cur) > maxLen and cur != '' and cur == cur[::-1]:
                out = cur
                maxLen = len(cur)
            else: continue
    print(maxLen)
    print(out)

