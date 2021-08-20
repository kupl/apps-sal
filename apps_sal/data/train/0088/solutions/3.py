n = int(input())
for x in map(int, input().split()):
    print('YES' if x > 14 and x % 14 > 0 and (x % 14 <= 6) else 'NO')
