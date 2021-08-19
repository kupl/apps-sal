s = input()
ans = True
cnt = 0
for (i, char) in enumerate(s):
    if i == 0:
        if char != 'A':
            ans = False
            break
    elif 2 <= i and i <= len(s) - 2:
        if char == 'C':
            cnt += 1
    elif char.isupper():
        ans = False
        break
if cnt == 1 and ans:
    print('AC')
else:
    print('WA')
