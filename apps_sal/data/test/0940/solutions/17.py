aa, bb, cc = list(map(int, input().split(" ")))
s = [aa, bb, cc]
s.sort()
a = s[0]
b = s[1]
c = s[2]

if c < a + b:
    print(0)
else:
    print(str(c - (a + b) + 1))
