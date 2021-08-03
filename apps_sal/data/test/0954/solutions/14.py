string = input()
a = set()
for i in range(len(string)):
    a.add(string[i:] + string[:i])
print(len(a))
