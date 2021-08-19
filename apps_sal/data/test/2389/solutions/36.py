(n, a, b, c) = list(map(int, input().split()))
l = []
for i in range(0, n):
    s = input()
    l.append(s)
final = []
for i in range(0, len(l)):
    if l[i] == 'AB':
        if a > b:
            b += 1
            a -= 1
            final.append('B')
        elif a < b:
            b -= 1
            a += 1
            final.append('A')
        elif a == 0:
            print('No')
            break
        elif i != len(l) - 1:
            if l[i + 1] == 'AB':
                a += 1
                b -= 1
                final.append('A')
            elif l[i + 1] == 'AC':
                a += 1
                b -= 1
                final.append('A')
            else:
                a -= 1
                b += 1
                final.append('B')
        else:
            a -= 1
            b += 1
            final.append('B')
    elif l[i] == 'AC':
        if a > c:
            c += 1
            a -= 1
            final.append('C')
        elif a < c:
            c -= 1
            a += 1
            final.append('A')
        elif a == 0:
            print('No')
            break
        elif i != len(l) - 1:
            if l[i + 1] == 'AB':
                a += 1
                c -= 1
                final.append('A')
            elif l[i + 1] == 'AC':
                a += 1
                c -= 1
                final.append('A')
            else:
                a -= 1
                c += 1
                final.append('C')
        else:
            a -= 1
            c += 1
            final.append('C')
    elif b > c:
        c += 1
        b -= 1
        final.append('C')
    elif b < c:
        c -= 1
        b += 1
        final.append('B')
    elif b == 0:
        print('No')
        break
    elif i != len(l) - 1:
        if l[i + 1] == 'AB':
            b += 1
            c -= 1
            final.append('B')
        elif l[i + 1] == 'BC':
            b += 1
            c -= 1
            final.append('B')
        else:
            b -= 1
            c += 1
            final.append('C')
    else:
        b -= 1
        c += 1
        final.append('C')
else:
    print('Yes')
    for i in range(0, len(final)):
        print(final[i])
