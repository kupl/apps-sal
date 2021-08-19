def pal(string):
    for k in range(len(string) // 2):
        if string[k] != string[len(string) - (k + 1)]:
            return False
    return True


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
            if len(cur) > maxLen and pal(cur):
                out = cur
                maxLen = len(cur)
            else:
                pass
    print(maxLen)
    print(out)
