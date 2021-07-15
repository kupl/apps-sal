n = int(input())
c = {'A': 0, 'F': 0, 'I': 0}
for ch in input():
    c[ch] += 1
if c['I'] == 0:
    print(c['A'])
elif c['I'] == 1:
    print(1)
else:
    print(0)
