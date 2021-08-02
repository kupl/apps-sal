s = input()
n = int(input())
d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
e = 'abcdefghijklmnopqrstuvwxyz'
for i in s:
    z = ord(i) - ord('a') if ord('a') <= ord(i) and ord(i) <= ord('z') else ord(i) - ord('A')
    if z < n:
        print(d[z], end='')
    else:
        print(e[z], end='')
