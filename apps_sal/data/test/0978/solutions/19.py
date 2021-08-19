a = int(input())
allp = ''
for i in range(4):
    allp += input()
okay = 'YES'
for i in range(9):
    if allp.count(str(i + 1)) > a * 2:
        okay = 'NO'
        break
print(okay)
