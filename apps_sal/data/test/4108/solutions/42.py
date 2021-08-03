s = input()
t = input()
cs = []
ct = []
for i in range(97, 97 + 26):
    cs.append(s.count(chr(i)))
    ct.append(t.count(chr(i)))
if sorted(cs) == sorted(ct):
    print("Yes")
else:
    print("No")
