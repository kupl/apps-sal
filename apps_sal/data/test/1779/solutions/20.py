import string
a, b, string = input(), input(), input()
l = len(string)
temp = string.lower().translate(string.maketrans(a, b))
for x in range(l):
    c = string[x]
    if c.lower() != c:
        temp = temp[:x] + temp[x].upper() + temp[x + 1:]
print(temp)
