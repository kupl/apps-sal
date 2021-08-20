c = int(input())
(*d,) = input().split()
if d.count('1') == c == 1 or (d.count('0') == 1 and c > 1):
    print('YES')
else:
    print('NO')
