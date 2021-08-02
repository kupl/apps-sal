n = input()
v = [int(i) for i in '2723342512']
s = '0' + n if len(n) == 1 else n
print(v[int(s[0])] * v[int(s[1])])
