import string
c = input()
abc = list(string.ascii_lowercase)
i = abc.index(c)

print(abc[i + 1])
