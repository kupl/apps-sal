import string
s = input()
t = set(s) ^ set(string.ascii_lowercase)
for i in string.ascii_lowercase:
    if set(i) & t:
        print(i)
        break
else:
    print('None')
