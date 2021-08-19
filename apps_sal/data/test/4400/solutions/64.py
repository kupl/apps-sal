import collections
S = input()
RainyDay = S.count('R')
if RainyDay == 2 and S[1] == 'S':
    RainyDay = 1
print(RainyDay)
