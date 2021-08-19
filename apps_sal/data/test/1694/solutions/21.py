(n, m, s, f) = map(int, input().split())
data = {}
for _ in range(m):
    (t, l, r) = map(int, input().split())
    data[t] = (l, r)
k = 1
curr = s
while curr != f:
    if k in data:
        if data[k][0] <= curr <= data[k][1]:
            print('X', end='')
        elif 1 < curr < n:
            if curr > f:
                if data[k][0] <= curr - 1 <= data[k][1]:
                    print('X', end='')
                else:
                    print('L', end='')
                    curr -= 1
            elif data[k][0] <= curr + 1 <= data[k][1]:
                print('X', end='')
            else:
                print('R', end='')
                curr += 1
        elif curr == 1:
            if data[k][0] <= 2 <= data[k][1]:
                print('X', end='')
            else:
                print('R', end='')
                curr = 2
        elif curr == n:
            if data[k][0] <= curr - 1 <= data[k][1]:
                print('X', end='')
            else:
                print('L', end='')
                curr -= 1
    elif curr > f:
        print('L', end='')
        curr -= 1
    else:
        print('R', end='')
        curr += 1
    k += 1
