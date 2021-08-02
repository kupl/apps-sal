S = input()
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
year = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
for i in range(10, 100):
    year.append(str(i))

if month.count(S[0:2]) == 1 and year.count(S[2:4]) == 1 and month.count(S[2:4]) == 1 and year.count(S[0:2]) == 1:
    print('AMBIGUOUS')
elif month.count(S[2:4]) == 1 and year.count(S[0:2]) == 1:
    print('YYMM')
elif month.count(S[0:2]) == 1 and year.count(S[2:4]) == 1:
    print('MMYY')
else:
    print('NA')
