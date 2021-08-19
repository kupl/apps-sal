from collections import defaultdict
kero = ['AC', 'WA', 'TLE', 'RE']
tanuki = defaultdict(int)
n = int(input())
s = [input() for i in range(n)]
for res in s:
    tanuki[res] += 1
for k in kero:
    print(f'{k} x {tanuki[k]}')
