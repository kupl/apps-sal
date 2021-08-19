_ = input()
s = input()
unique = len(set(s))
if len(s) > 26:
    print(-1)
else:
    print(len(s) - unique)
