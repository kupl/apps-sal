from collections import *
for _ in range(int(input())):
    print('First' if int(input()) % 2 ^ any((v % 2 for v in Counter(map(int, input().split())).values())) else 'Second')
