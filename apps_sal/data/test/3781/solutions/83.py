i = input
for _ in range(int(i())):
    print('First' if int(i()) % 2 ^ ((a := sorted(map(int, i().split())))[::2] != a[1::2]) else 'Second')
