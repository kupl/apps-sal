s = sorted(list(input()))
t = sorted(list(input()), reverse=True)
if s < t:
    print('Yes')
else:
    print('No')
