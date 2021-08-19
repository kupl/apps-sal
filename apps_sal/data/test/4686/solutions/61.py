s = input()
di = {}
for c in s:
    di[c] = 0
for c in s:
    di[c] += 1
is_beautiful = True
for c in s:
    if di[c] % 2 == 1:
        is_beautiful = False
print('Yes' if is_beautiful else 'No')
