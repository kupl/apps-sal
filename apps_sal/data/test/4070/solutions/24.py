a = int(input())
a = str(hex(a))
s = 0
for i in range(1, len(a)):
    if a[i] in ['0', '4', '6', '9', 'a', 'd']:
        s = s + 1
    if a[i] in ['8', 'b']:
        s = s + 2
print(s)
