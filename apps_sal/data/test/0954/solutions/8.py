w = input()
s = set()
for shift in range(len(w)):
    s.add(w[-shift:] + w[:-shift])
print(len(s))
