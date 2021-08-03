N = 9999999999999999999999999999999999999984
n, m = tuple(map(int, input().split()))
memory = set()
for _ in range(n):
    su = 0
    p = 1
    entry = input()
    for letter in entry:
        su = (su + p * ord(letter)) % N
        p = (p * 203) % N
    p = 1
    for letter in entry:
        for i in ['a', 'b', 'c']:
            if i != letter:
                memory.add((p * (ord(i) - ord(letter)) + su) % N)
        p = (p * 203) % N
answer = []
for _ in range(m):
    su = 0
    p = 1
    for letter in input():
        su = (su + p * ord(letter)) % N
        p = (p * 203) % N
    if su in memory:
        answer.append('YES')
    else:
        answer.append('NO')

print('\n'.join(answer))
