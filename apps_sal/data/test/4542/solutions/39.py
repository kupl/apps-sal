S = input()

s = S.replace('WB', 'W B').replace('BW', 'B W')
s = list(s.split())
print(len(s) -1)
