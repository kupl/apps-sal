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
            if i + j > n:
                break
            cur = s[i:i + j]
            if len(cur) > maxLen and cur == cur[::-1]:
                out = cur
                maxLen = len(cur)
            else:
                pass
    print(maxLen)
    print(out)
