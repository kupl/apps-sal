import sys
input = sys.stdin.readline

S = list(input().rstrip('\n'))

kake10 = [0, 10, 7, 4, 1, 11, 8, 5, 2, 12, 9, 6, 3]
now = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
for i in S:
    now = {kake10[x]: now[x] for x in range(13)}
    if i == '?':
        now2 = {x: sum(now[(x + y) % 13] for y in range(4, 14)) % 1000000007 for x in range(13)}
        now = now2
    else:
        a = int(i)
        now = {(x + a) % 13: now[x] for x in range(13)}
print(now[5])
