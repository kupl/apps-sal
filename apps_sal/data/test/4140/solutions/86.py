s = input()
os = s[1::2]
es = s[::2]
l = os.count('0') + es.count('1')
print(min(l, len(s) - l))
