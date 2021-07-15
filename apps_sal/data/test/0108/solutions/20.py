import math

s = input()
alf = "abcdefghijklmnopqrstuvwxyz"
n = -1

def con_str(string, ch, i):
    return string[:i] + ch + string[i+1:]

for i in alf:
    flag = False
    for j in range(n+1, len(s)):
        if s[j]<=i:
            n = j
            s = con_str(s, i, j)
            flag = True
            break
    if not(flag):
        print(-1)
        return
print(s)
