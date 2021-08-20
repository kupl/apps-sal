n = ''
command = input()
for i in command:
    if i == 'B':
        n = n[:-1]
    else:
        n += i
print(n)
