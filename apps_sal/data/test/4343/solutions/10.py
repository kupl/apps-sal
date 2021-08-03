n = int(input())
s = [ord(c) - 97 for c in input()]
t = [ord(c) - 97 for c in input()]
a = []
b = 0
p = n - 1
temp = t[p] + s[p]
while p > 0:
    p -= 1
    temp += (t[p] + s[p]) * 26
    a.append(chr(int(temp / 2) % 26 + 97))
    temp //= 26
a.append(chr(int(temp / 2) % 26 + 97))
p = n
while p:
    p -= 1
    print(a[p], end='')
