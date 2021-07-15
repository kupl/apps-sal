n = int(input())
for q in range(n):
    a = input()
    if sum([int(q) for q in a]) % 3 != 0:
        print('cyan')
    elif a.count('0') == 0:
        print('cyan')
    else:
        w = a.find('0')
        a = a[:w]+a[w+1:]
        if any(q in ['0', '2', '4', '6', '8'] for q in a):
            print('red')
        else:
            print('cyan')

