s1 = input()
s2 = input()
a = {}
for i in range(len(s1)):
    a[s1[i].lower()] = s2[i].lower()
    a[s1[i].upper()] = s2[i].upper()
ans1 = input()
for i in ans1:
    if i in a:
        print(a[i], end = "")
    else:
        print(i, end = "")

