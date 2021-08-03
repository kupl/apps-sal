s = input()
k = list(set(s))
if len(k) == 2 and s.count(k[0]) == 2:
    print("Yes")
else:
    print("No")
