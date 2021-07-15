s = input()
t = ''
if len(s) % 2:
    start = True
else:
    start = False
s = list(s)
while s:
    if start:
        t = s.pop(0) + t
        start = False
    else:
        t = s.pop() + t
        start = True
print(t)
