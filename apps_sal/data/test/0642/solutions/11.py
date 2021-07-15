3

def readln(): return tuple(map(int, input().split()))

n, m = readln()
d = sorted(readln()) if m else []
if m and (d[0] == 1 or d[-1] == n) or m > 2 and [1 for i, j, k in zip(d[:-2], d[1:-1], d[2:]) if i + 2 == k]:
    print('NO')
else:
    print('YES')

