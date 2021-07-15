N = int(input())
S = input()
ls = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lsS = list(S)
lsans = []
for i in range(len(S)):
    lsans.append(ls[(ls.index(lsS[i])+N) % 26])
print(''.join(lsans))
