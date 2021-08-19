t = 'iloveyou'
p = 1
s = input()
for i in t:
    if i not in s:
        p = 0
        break
if p is 1:
    print('happy')
else:
    print('sad')
