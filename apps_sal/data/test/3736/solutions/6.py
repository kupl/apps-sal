p, t = 'AHIMOTUVWXY', input()
n = len(t) // 2
print('YES' if all(c in p for c in t) and (n < 1 or t[: n][:: -1] == t[-n :]) else 'NO')
