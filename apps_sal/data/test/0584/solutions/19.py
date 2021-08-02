import re
l = input()
S = input()
a = [word for e in re.split(r"\([^()]*\)", S) for word in re.split(r"_+", e)]
b = [word for e in re.findall(r"\([^()]*\)", S) for word in re.split(r"_+", e[1:-1]) if word]
print(str(len(max(a, key=len))) + " " + str(len(b)))
