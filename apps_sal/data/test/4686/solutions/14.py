w = input()
a = 'abcdefghijklmnopqrstuvwxyz'
b = 0
for i in range(26):
    if w.count(a[i]) % 2 == 0:
        b += 0
    else:
        b += 1
print('Yes' if b == 0 else 'No')
