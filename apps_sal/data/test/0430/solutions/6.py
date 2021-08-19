a = int(input())
b = list(map(int, input().split()))
big = b.count(200)
s = b.count(100)
if big % 2 == 0 and s % 2 == 0 or (s % 2 == 0 and s >= 2):
    print('YES')
else:
    print('NO')
