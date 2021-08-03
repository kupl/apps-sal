s = ''.join(sorted(input()))
t = ''.join(reversed(sorted(input())))

if s < t:
    print('Yes')
else:
    print('No')
