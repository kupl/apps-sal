def readln(): return tuple(map(int, input().split()))


n, s = readln()
a = readln()
print('YES' if sum(a) - max(a) <= s else 'NO')
