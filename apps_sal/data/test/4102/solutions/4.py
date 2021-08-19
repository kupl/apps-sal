m = {}
m['0'] = '8'
m['1'] = 'x'
m['2'] = 'x'
m['3'] = '3'
m['4'] = '6'
m['5'] = '9'
m['6'] = '4'
m['7'] = '7'
m['8'] = '0'
m['9'] = '5'
x = list(input())
y = list(reversed([m[c] for c in x]))
print('Yes' if x == y else 'No')
