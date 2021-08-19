import re
l = input()
S = input()
a = [word for e in re.split('\\([^()]*\\)', S) for word in re.split('_+', e)]
b = [word for e in re.findall('\\([^()]*\\)', S) for word in re.split('_+', e[1:-1]) if word]
print(str(len(max(a, key=len))) + ' ' + str(len(b)))
