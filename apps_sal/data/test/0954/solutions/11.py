string = input()
s = set()
for i in range(len(string)):
    if string not in s:
        s.add(string)
    string = string[len(string) - 1] + string[:-1]
print(len(s))
