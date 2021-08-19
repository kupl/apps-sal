a = str(input())
b = list(str(input()))
b.pop(-1)
b = ''.join(b)
if a == b:
    print('Yes')
else:
    print('No')
