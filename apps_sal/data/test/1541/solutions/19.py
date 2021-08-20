s = input()
for i in range(len(s)):
    if s[i] == '^':
        o = i
l = s[0:o]
r = s[o + 1:len(s)]
l_sum = r_sum = 0
for i in range(len(l)):
    if not l[i] == '=':
        l_sum += int(l[i]) * (len(l) - i)
for i in range(len(r)):
    if not r[i] == '=':
        r_sum += int(r[i]) * (i + 1)
if l_sum < r_sum:
    print('right')
elif l_sum > r_sum:
    print('left')
else:
    print('balance')
