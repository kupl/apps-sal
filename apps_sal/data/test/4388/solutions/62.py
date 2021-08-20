n = input()
s = ''
for i in range(3):
    if n[i] == '1':
        s = s + '9'
    else:
        s = s + '1'
print(s)
