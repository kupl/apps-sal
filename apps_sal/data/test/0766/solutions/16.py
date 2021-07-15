s = input()
a = set()
for i in s:
    a.add(i)
a = list(a)
if len(a) == 4:
    print("Yes")
elif len(a) == 2:
    if s.count(a[0]) > 1 and s.count(a[1]) > 1:
        print("Yes")
    else:
        print("No")
elif len(a) == 3:
    if s.count(a[0]) > 1 or s.count(a[1]) > 1 or s.count(a[2]) > 1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
