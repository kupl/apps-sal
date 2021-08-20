import io
import os


def check(d):
    for i in range(len(s) - d + 1):
        pos = 0
        for x in s[:i]:
            if x == s1[pos]:
                pos += 1
                if pos == len(s1):
                    return True
        for x in s[i + d:]:
            if x == s1[pos]:
                pos += 1
                if pos == len(s1):
                    return True
    return False


s = input()
s1 = input()
l = 0
r = len(s)
while r - l > 1:
    mid = (r + l) // 2
    if check(mid):
        l = mid
    else:
        r = mid
print(l)
'\ncheck(3)\n'
