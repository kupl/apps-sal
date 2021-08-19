s = input().rstrip()
t = input().rstrip()
s = tuple(sorted(s))
t = tuple(sorted(t, reverse=True))
if s < t:
    print('Yes')
else:
    print('No')
