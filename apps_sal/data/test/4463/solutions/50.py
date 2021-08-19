list_s = sorted(list(input()))
list_t = sorted(list(input()), reverse=True)
if ''.join(list_s) < ''.join(list_t):
    print('Yes')
else:
    print('No')
