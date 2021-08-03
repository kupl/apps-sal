__author__ = 'Utena'
M = 100000000000007


def hash(x):
    a = 0
    for j1 in x:
        a = (a * 1003 + ord(j1)) % M
    return a


def get(q):
    l = len(q)
    e = 1
    h = hash(q)
    for j in range(1, l + 1):
        aj = q[-j]
        a, b, c = ((h + (e * (ord('a') - ord(aj)))) + M * 2) % M, ((h + (e * (ord('b') - ord(aj)))) + M * 2) % M, ((h + (e * (ord('c') - ord(aj)))) + M * 2) % M
        e = (e * 1003) % M
        if aj == 'a':
            if b in search[l] or c in search[l]:
                return 'YES'
        elif aj == 'b':
            if a in search[l] or c in search[l]:
                return 'YES'
        elif aj == 'c':
            if a in search[l] or b in search[l]:
                return 'YES'
    return 'NO'


ans = []
n, m = map(int, input().split())
search = [set()for i in range(600001)]
for i in range(n):
    s = input()
    search[len(s)].add(hash(s))
for i in range(m):
    q = input()
    ans.append(get(q))
print('\n'.join(ans))
