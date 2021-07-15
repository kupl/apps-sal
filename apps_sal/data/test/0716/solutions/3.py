n, a, b = [int(x) for x in input().split()]
s = input()
if (s[a - 1] != s[b - 1]):
    print('1')
else: print('0')
