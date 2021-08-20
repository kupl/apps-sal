[copies, originals] = input().split()
copies = int(copies)
originals = int(originals)
if originals < 1:
    print('No')
elif originals == 1 and copies > 0:
    print('No')
elif originals > copies + 1:
    print('No')
elif (copies - originals) % 2 == 0:
    print('No')
else:
    print('Yes')
