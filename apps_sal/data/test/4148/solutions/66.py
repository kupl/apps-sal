n = int(input())
s = list(input())
li = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'
,'R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'
,'R','S','T','U','V','W','X','Y','Z']
li1 = []
for i in s:
    li1.append(li[li.index(i)+n])

print((''.join(li1)))

