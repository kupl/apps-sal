'''
Created on ٣١‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
n = int(t[0])
m = int(t[1])

s = set()
u = set(i for i in range(1, n + 1))

for i in range(m):
    t = input().split()
    s.add(int(t[0]))
    s.add(int(t[1]))
uniq = (u - s).pop()

print(n - 1)
for i in range(1, n + 1):
    if i != uniq:
        print(i, uniq)
