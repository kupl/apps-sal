ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
S = input()
for s in S:
    print(ALP[ALP.index(s) + n], end='')
