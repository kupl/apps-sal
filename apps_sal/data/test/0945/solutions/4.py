n = int(input())
a = list(map(int, input().split()))
if n <= 3:
    print('no')
else:
    fg = 0
    for i in range(n-3):
        for j in range(i+2, n-1):
            if min(a[i], a[i+1]) < min(a[j], a[j+1]) < max(a[i], a[i+1]) < max(a[j], a[j+1]) or min(a[j], a[j+1]) < min(a[i], a[i+1]) < max(a[j], a[j+1]) < max(a[i], a[i+1]):
                fg = 1
                break;
        if fg: break;

    if fg: print('yes')
    else: print('no')


