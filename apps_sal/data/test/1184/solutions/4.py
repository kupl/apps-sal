s = set()
string = input().rstrip()
i = 1
while i < len(string):
    s.add(string[i])
    i += 3
if string == "{}":
    print(0)
else:
    print(len(s))
