s = str(input())
for cont in range(0,len(s)):
    if s[cont] == '^':
        pos = cont
        break

left = 0
right = 0
for d in range(0, pos):
    if s[d].isdigit():
        left += int(s[d])*(pos-d)

for d in range(pos+1,len(s)):
    if s[d].isdigit():
        right += int(s[d])*(d-pos)

if left == right:
    print('balance')
elif right> left:
    print('right')
else:
    print('left')
