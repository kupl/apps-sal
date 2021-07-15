n = int(input())

ratings = []
divs = []

for i in range(n):
    a, b = map(int, input().split())
    ratings.append(a)
    divs.append(b)

curmax = float('inf')
curmin = float('-inf')

if n == 1:
    if divs[0] == 1:
        print('Infinity')
    else:
        print(1899 + ratings[0])
else:
    for k in range(n - 1):
        st = divs[k]
        fin = divs[k + 1]
        change = ratings[k]

        if st == 1 and fin == 2:
            if change >= 0:
                print('Impossible')
                break
            curmax = min(curmax + change, 1899)
            curmin = max(curmin + change, 1900 + change)
        elif st == 2 and fin == 2:
            curmax = min(curmax + change, 1899, 1899 + change)
            curmin += change
        elif st == 1 and fin == 1:
            curmin = max(curmin + change, 1900, 1900 + change)
            curmax += change
        elif st == 2 and fin == 1:
            if change <= 0:
                print('Impossible')
                break
            curmax = min(curmax + change, 1899 + change)
            curmin = max(curmin + change, 1900)
    else:
        if curmax == float('inf'):
            print('Infinity')
        elif curmin > curmax:
            print('Impossible')
        else:
            print(curmax + ratings[-1])
