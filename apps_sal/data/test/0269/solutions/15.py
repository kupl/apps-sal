s = input()
cols = ['R', 'B', 'Y', 'G']
result = dict([(c, 0) for c in cols])
num_to_cols = dict()
for c in cols:
    num_to_cols[s.find(c) % 4] = c
for lnum in range(len(s)):
    if s[lnum] == '!':
        result[num_to_cols[lnum % 4]] += 1
print(result['R'], result['B'], result['Y'], result['G'])
