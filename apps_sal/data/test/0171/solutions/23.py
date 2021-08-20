s = input().strip()
alp = set([chr(i) for i in range(ord('a'), ord('z') + 1)])
upper = set([chr(i) for i in range(ord('A'), ord('Z') + 1)])
num = set([str(i) for i in range(10)])
if len(s) >= 5:
    s = set(list(s))
    if len(s & alp) > 0 and len(s & upper) > 0 and (len(s & num) > 0):
        print('Correct')
    else:
        print('Too weak')
else:
    print('Too weak')
