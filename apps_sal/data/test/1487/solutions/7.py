s = input()
t = input()
if s == t:
    print(s)
    return
p = []
dif = 0
for i in range(len(s)):
    if s[i] != t[i]:
        dif += 1

if dif % 2 == 1:
    print("impossible")
    return
prev = True
for i in range(len(s)):
    if s[i] == t[i]:
        p.append(s[i])
    else:
        if dif:
            p.append(s[i] if prev else t[i])
            prev = False if prev else True
print("".join(p))
