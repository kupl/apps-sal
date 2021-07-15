s = input()
open = {'(', '{', '[', '<'}
res = 0
our = []
for elem in s:
    if elem in open:
        our.append(elem)
    else:
        if our:
            res += (abs(ord(elem) - ord(our[-1])) > 2)
            our.pop()
        else:
            print('Impossible')
            return
if our:
    print('Impossible')
else:
    print(res)
