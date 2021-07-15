s = input()[1:-1]
if len(s) == 0:
    print(0)
else:
    print(len(set(s.split(', '))))
