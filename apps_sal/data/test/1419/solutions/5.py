n = int(input())
s = input()
s += ' '


def ok(w):
    wordcnt = 0
    lettercnt = 0
    linecnt = 0
    for j in range(len(s)):
        if not (s[j] == ' ' or s[j] == '-'):
            lettercnt += 1
        else:
            lettercnt += 1
            if j == len(s) - 1:
                lettercnt -= 1
            if (wordcnt + lettercnt) > w:
                linecnt += 1
                wordcnt = lettercnt
            else:
                wordcnt += lettercnt
            lettercnt = 0
        if wordcnt > w:
            return False

    if wordcnt:
        linecnt += 1
    if linecnt > n:
        return False
    else:
        return True


l = 1
r = 1000000
while l < r:
    mid = l + (r - l) // 2
    if ok(mid):
        r = mid
    else:
        l = mid + 1
print(l)
