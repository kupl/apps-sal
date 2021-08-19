n = int(input())
a = list(map(int, input().split()))
a.sort()
s = []
for i in range(0, len(a) // 2):
    s.append(a[i])
    s.append(a[len(a) - 1 - i])
if n % 2 == 1:
    s.append(a[len(a) // 2])
Po = 1
for k in range(2, len(s) - 1):
    if k % 2 == 1:
        if s[k] >= s[k - 1]:
            pass
        else:
            print('Impossible')
            Po = 0
            break
    elif k == 1:
        pass
    elif s[k] <= s[k - 1]:
        pass
    else:
        print('Impossible')
        Po = 0
        break
if Po == 1:
    print(' '.join(map(str, s)))
