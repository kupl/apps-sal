(n, m) = [int(x) for x in input().split()]
S = set()
for i in range(n):
    S.update({int(x) for x in input().split()[1:]})
print('YES' if S == set(range(1, m + 1)) else 'NO')
