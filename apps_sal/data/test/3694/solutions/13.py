n = int(input())
a = sorted(list(map(int, input().split())))

win = None
first = True

if n == 1:
    win = a[0] % 2 == 1
elif a[1] == 0:
    win = False

if n > 2:
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            if i > 0:
                if a[i - 1] == a[i] - 1:
                    win = False
                    break
            if not first:
                win = False
                break
            first = False


if win is None:
    win = (sum(a) - (n * (n - 1) // 2)) % 2 == 1

if win:
    print('sjfnb')
else:
    print('cslnb')
