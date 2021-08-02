n, a, b = list(map(int, input().split(' ')))
s = input()

if a == b or s[a - 1] == s[b - 1]: print('0')
else: print('1')
