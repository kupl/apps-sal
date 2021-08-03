s = list(input())
n = len(s)
d = ''
prev = -1
if n % 2 == 0:
    d += s.pop(n - 1)
while s != []:
    if prev == -1:
        d += s.pop(0)
        prev = 0
    else:
        d += s.pop(len(s) - 1)
        prev = -1
print(d[::-1])
