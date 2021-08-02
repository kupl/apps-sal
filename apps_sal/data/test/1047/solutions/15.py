import sys
f = sys.stdin

s = f.readline().strip()
si = []
for i in range(len(s)):
    si.append(int(s[i]))

r = []

for k in range(9):
    ki = 0
    for i in range(len(si)):
        if si[i] > 0:
            si[i] -= 1
            ki += 10**(len(si) - i - 1)
    if ki == 0:
        break
    r.append(str(ki))


print(len(r))
print(' '.join(r))
