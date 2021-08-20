import sys
fin = sys.stdin
(a, b) = (fin.readline().rstrip().lstrip('0'), fin.readline().rstrip().lstrip('0'))
if len(a) < len(b):
    print('<')
elif len(a) > len(b):
    print('>')
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] < b[i]:
            print('<')
            break
        else:
            print('>')
            break
    else:
        print('=')
