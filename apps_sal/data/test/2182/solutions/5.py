n = int(input())

for qwe in range(n):
    a = list(sorted(list(map(int, input()))))
    if sum(a) % 3 == 0 and a[0] == 0 and (0 in a[1:] or 2 in a[1:] or 4 in a[1:] or 6 in a[1:] or 8 in a[1:]):
        print('red')
    else:
        print('cyan')
