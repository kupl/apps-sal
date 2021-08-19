s = ''.join(sorted(str(input())))
t = ''.join(sorted(str(input()), reverse=True))
if s < t:
    print('Yes')
else:
    print('No')
