from collections import Counter

S = list(input())
ac = Counter(S)

alp = 'abcdefghijklmnopqrstuvwxyz'

for a in alp:
    if not(a in ac):
        print(a)
        break
else:
    print('None')
