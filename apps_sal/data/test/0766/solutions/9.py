from collections import Counter

s = input()
ln = len(set(s))
C = Counter(s)

if ln == 1 or ln > 4:
    print('No')

elif ln == 2:
    print(('No', 'Yes')[min(C.values()) >= 2])

elif ln == 3:
    print(('No', 'Yes')[max(C.values()) >= 2])

elif ln == 4:
    print('Yes')

else:
    exit(100500)

