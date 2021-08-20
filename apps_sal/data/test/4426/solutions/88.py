S = input()
lst = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
dct = {}
for (i, j) in enumerate(lst):
    dct[j] = i
print(7 - dct[S])
