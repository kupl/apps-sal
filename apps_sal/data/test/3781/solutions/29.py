i = input
t = int(i())
for _ in range(t):
    print('First' if int(i()) % 2 ^ ((a := sorted(map(int, i().split())))[::2] != a[1::2]) else 'Second')
