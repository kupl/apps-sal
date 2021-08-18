import sys
input = sys.stdin.readline


def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getList(): return list(map(int, input().split()))
def getStr(): return input().strip()


n = getInt()
for i in range(n):
    s, c = getStr().split()
    p = False
    for i in range(len(s) - 1):
        ch = i
        for j in range(i + 1, len(s)):
            if s[j] <= s[ch]:
                ch = j
        if s[ch] < s[i]:
            s = s[:i] + s[ch] + s[i + 1:ch] + s[i] + s[ch + 1:]
            break
    if s < c:
        print(s)
    else:
        print('---')
