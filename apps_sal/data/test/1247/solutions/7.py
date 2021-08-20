3
s = sorted(list(input()))
tmp = [len([1 for i in s if c == i]) % 2 for c in set(s)]
if sum(tmp) == 0 or sum(tmp) % 2 == 1:
    print('First')
else:
    print('Second')
