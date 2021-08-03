string = input()

a = string.count('a')
b = string.count('b')
c = string.count('c')

ad = False
bd = False
cd = False

ans = True

ba = string.count('ba')
cb = string.count('cb')
ca = string.count('ca')


if (a > 0) and (b > 0) and ((a == c) or (b == c)) and (ba == 0) and (cb == 0) and (ca == 0):
    print('YES')
else:
    print('NO')
