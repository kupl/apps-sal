s = input()
tmp = ''
s = s[::-1]
xx = z = it = 0
for c in s:
    if c == '2':
        tmp = tmp + '0' * z + '2'
        z = 0
    if c == '0':
        z += 1
    if c == '1':
        xx += 1
    it = it + 1
tmp = tmp + '1' * xx + '0' * z
print(tmp[::-1])
