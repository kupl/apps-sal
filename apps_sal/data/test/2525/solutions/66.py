s = list(input())
q = int(input())
rv = False
right = []
left = []
for _ in range(q):
    query = input()
    if query[0] == '1':
        rv = not rv
    else:
        (_, f, c) = query.split()
        if f == '1' and rv == False:
            left.append(c)
        elif f == '1' and rv == True:
            right.append(c)
        elif f == '2' and rv == False:
            right.append(c)
        elif f == '2' and rv == True:
            left.append(c)
if not rv:
    left.reverse()
    print(''.join(left) + ''.join(s) + ''.join(right))
else:
    right.reverse()
    s.reverse()
    print(''.join(right) + ''.join(s) + ''.join(left))
