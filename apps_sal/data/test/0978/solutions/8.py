3


def readln(): return tuple(map(int, input().split()))


k, = readln()
cnt = {}
for c in list(''.join([input() for _ in range(4)])):
    if c != '.':
        cnt[c] = cnt.get(c, 0) + 1
print('YES' if len([1 for v in list(cnt.values()) if v <= 2 * k]) == len(cnt) else 'NO')
