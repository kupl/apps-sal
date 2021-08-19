import sys
n = int(sys.stdin.readline())
s = list(sys.stdin.readline())
s = s[:-1]
r = 0
k = [0] * 26
o = [0] * 26
j = 0
for i in s:
    if j % 2 == 0:
        k[ord(i) - 97] = k[ord(i) - 97] + 1
    elif k[ord(i) - 65] > 0:
        k[ord(i) - 65] = k[ord(i) - 65] - 1
    else:
        r = r + 1
    j = j + 1
print(r)
