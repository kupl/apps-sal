from sys import stdin, stdout

n = int(stdin.readline().rstrip())
cards = []
for _ in range(n):
    cards.append(int(stdin.readline().rstrip()))
    
n1 = max(cards)
n2 = min(cards)

c1 = cards.count(n1)
c2 = cards.count(n2)

if c1==c2 and c1+c2==n and n1!=n2:
    print('YES')
    print(str(n1) + ' ' + str(n2))
else:
    print('NO')

