firstline = [int(x) for x in input().split()]
firstnum = 0
for digit in input().split():
    firstnum *= firstline[1]
    firstnum += int(digit)

secondline = [int(x) for x in input().split()]
secondnum = 0

for digit in input().split():
    secondnum *= secondline[1]
    secondnum += int(digit)

if (firstnum > secondnum):
    print('>')
if (firstnum == secondnum):
    print('=')
if (firstnum < secondnum):
    print('<')
