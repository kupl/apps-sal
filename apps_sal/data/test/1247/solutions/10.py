from string import ascii_lowercase
s = input()
k = 0
for c in ascii_lowercase:
    if s.count(c) % 2 != 0:
        k += 1
if k == 0 or k == 1 or k % 2 != 0:
    print('First')
else:
    print('Second')
