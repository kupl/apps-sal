(n, m) = input().split()
(n, m) = (int(n), int(m))
s = set()
for a in range(n):
    s |= set(input().split()[1:])
for b in range(m):
    if str(b + 1) in s:
        continue
    else:
        print('NO')
        quit()
print('YES')
