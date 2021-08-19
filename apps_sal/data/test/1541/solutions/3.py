x = input()
ind = x.index('^')
w1 = x[0:ind]
w2 = x[ind + 1:]
left = 0
right = 0
for i in range(0, ind):
    if x[i] == '=':
        left += 0
    else:
        left += int(x[i]) * (ind - i)
for j in range(ind + 1, len(x)):
    if x[j] == '=':
        right += 0
    else:
        right += int(x[j]) * (j - ind)
if left > right:
    print('left')
if left < right:
    print('right')
if left == right:
    print('balance')
