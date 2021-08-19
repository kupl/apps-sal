__author__ = 'Rakshak.R.Hegde'
'\nCreated on Jan 12 2015 PM 02:41\n\n@author: Rakshak.R.Hegde\n'
changes = []
valids = []
for t in range(int(input())):
    (a, b) = input().split()
    do = True
    for i in changes:
        if b == (i[0] or i[1]):
            do = False
            break
        if i[1] == a:
            i[1] = b
            break
    else:
        if do:
            changes.append([a, b])
print(len(changes))
for change in changes:
    print(change[0], change[1])
