l = list(input().split())
if len(set(l)) == 1:
    print('=')
elif l == sorted(l):
    print('<')
else:
    print('>')
