from collections import defaultdict
(n, m) = (int(t) for t in input().split(' '))
m1 = [[int(t) for t in input().split(' ')] for _ in range(n)]
m2 = [[int(t) for t in input().split(' ')] for _ in range(n)]


def get_csum(mx):
    csum = [defaultdict(int) for _ in range(n + m + 1)]
    for i in range(n):
        for j in range(m):
            csum[i + j][mx[i][j]] += 1
    return csum


csum1 = get_csum(m1)
csum2 = get_csum(m2)
print('YES' if csum1 == csum2 else 'NO')
