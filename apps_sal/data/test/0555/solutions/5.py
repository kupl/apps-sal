n = input()
new = ''
l = len(n)

if n[0] != '9':
    if int(n[0]) > 9 - int(n[0]):
        new += str(9 - int(n[0]))
    else:
        new += n[0]
else:
    new += n[0]

for i in range(1, l):
    if int(n[i]) > 9 - int(n[i]):
        new += str(9 - int(n[i]))
    else:
        new += n[i]

print(new)
