# Pye
from os import path
from sys import stdin, stdout
if path.exists('inp.txt'): stdin = open("inp.txt", "r")
def io(): return stdin.readline()


maxn = 100005
ans = 0
q = int(io())
inp = io().split(); s = inp[0]
for i in range(25, 0, -1):
    check = 1
    while check:
        check = 0
        for j in range(len(s)):
            if j >= len(s): break
            if ord(s[j]) - ord('a') == i and j + 1 < len(s) and ord(s[j + 1]) - ord('a') == i - 1:
                s = s[0:j:] + s[j + 1::]
                ans += 1
                check = 1
            elif ord(s[j]) - ord('a') == i and j > 0 and ord(s[j - 1]) - ord('a') == i - 1:
                s = s[0:j:] + s[j + 1::]
                ans += 1
                check = 1
print(ans)
