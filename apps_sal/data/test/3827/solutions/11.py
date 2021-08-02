s = input()
a = 0
b = 0
c = 0
i = 0
while i < len(s) and s[i] == 'a':
    a += 1
    i += 1
while i < len(s) and s[i] == 'b':
    b += 1
    i += 1
while i < len(s) and s[i] == 'c':
    c += 1
    i += 1
if i == len(s) and (a == c or b == c) and a * b != 0:
    print("YES")
else:
    print("NO")
