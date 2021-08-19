import sys
input = sys.stdin.readline
s = input().strip()
maxlen = 0


def checkpalin(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


for i in range(len(s)):
    for j in range(i, len(s)):
        if not checkpalin(s[i:j + 1]):
            maxlen = max(maxlen, len(s[i:j + 1]))
print(maxlen)
