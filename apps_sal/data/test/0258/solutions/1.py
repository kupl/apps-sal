n = int(input())
a = input()
if a.count('?') % 2 == 1:
    print('Monocarp')
else:
    x = y = k = m = 0
    for q in range(n):
        if q * 2 < n:
            if a[q] == '?':
                k += 1
            else:
                x += int(a[q])
        elif a[q] == '?':
            m += 1
        else:
            y += int(a[q])
    if (y - x) % 9 == 0 and (y - x) // 9 == (k - m) // 2:
        print('Bicarp')
    else:
        print('Monocarp')
