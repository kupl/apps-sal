import re
s = input()
print(eval(s) + eval(re.sub("\d", "0", s).replace("-", "*3").replace("+", "-5").replace("*", "+")))
