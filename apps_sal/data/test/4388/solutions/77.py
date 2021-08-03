n = input()
i = 0
a = n[i].replace('1', '9') if n[i] == '1' else n[i].replace('9', '1')
i = 1
b = n[i].replace('1', '9') if n[i] == '1' else n[i].replace('9', '1')
i = 2
c = n[i].replace('1', '9') if n[i] == '1' else n[i].replace('9', '1')
print(a + b + c)
