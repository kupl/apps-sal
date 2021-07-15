seq = input()
zCount = 0
hasLead = False
for i in range(1, len(seq)+1):
    if seq[-i] == '0':
        zCount += 1
    if zCount >= 6 and seq[-i] == '1':
        hasLead = True
if hasLead:
    print('yes')
else:
    print('no')

