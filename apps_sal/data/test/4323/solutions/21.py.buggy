import sys
s = input().split()
n = int(s[0])
m = int(s[1])
siz = 0
dec = [None] * n
for i in range(n):
    s = input().split()
    siz += int(s[0])
    dec[i] = int(s[1]) - int(s[0])
dec.sort()
if siz <= m:
    print(0)
    return
for i in range(n):
    siz += dec[i]
    if siz <= m:
        print(i + 1)
        return
print(-1)
