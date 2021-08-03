N = input()
residue = 0
for i in N:
    residue = (residue + int(i)) % 9
if residue == 0:
    print('Yes')
else:
    print('No')
