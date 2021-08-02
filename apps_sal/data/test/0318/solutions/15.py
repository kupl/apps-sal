s = input()
n = int(input())
h = int(s[0:2])
m = int(s[3:])


h += ((m + n) // 60)
h %= 24
m = (m + n) % 60
s = ''
if len(str(h)) < 2:
    s += '0'
s += str(h) + ':'
if len(str(m)) < 2:
    s += '0'
s += str(m)
print(s)
