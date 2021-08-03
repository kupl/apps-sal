s = input()
sset = list(set(s))
print(("Yes" if len(sset) == 2 and s.count(sset[0]) == s.count(sset[1]) == 2 else "No"))
