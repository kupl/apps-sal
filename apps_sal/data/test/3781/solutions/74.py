from collections import *
i = input
for _ in range(int(i())):
    print('First' if int(i()) % 2 ^ any((v % 2 for v in Counter(map(int, i().split())).values())) else 'Second')
