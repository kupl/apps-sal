[n] = [int(w) for w in input().split()]
a = [int(w) for w in input().split()]
t = max(a)
s = sum(a)
r = s % 2 == 0 and s >= 2 * t
print('YES' if r else 'NO')
