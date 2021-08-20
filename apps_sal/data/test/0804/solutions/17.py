(s, k) = (input(), int(input()))
ss = set(s)
if len(s) < k:
    print('impossible')
else:
    print(max(k - len(ss), 0))
