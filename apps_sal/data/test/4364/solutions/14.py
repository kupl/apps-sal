S = str(input())
year = int(S[0] + S[1])
month = int(S[2] + S[3])
if year <= 12 and year >= 1 and month >= 1 and month <= 12:
    print('AMBIGUOUS')
elif year >= 0 and year <= 99 and month >= 1 and month <= 12:
    print('YYMM')
elif year >= 1 and year <= 12 and month >= 0 and month <= 99:
    print('MMYY')
else:
    print('NA')
