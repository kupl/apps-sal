s = input()
t = True
for i in s:
    if s.count(i) != 1:
        t = False
print("yes" if t else "no")
