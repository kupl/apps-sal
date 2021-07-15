input()
s = input()
s = s.lower()
all = set()
for i in s:
    all.add(i)
if len(all) == 26:
    print("YES")
else:
    print("NO")
