def win(a, b):
    if a == 'R':
        if b == 'P': return 'P'
        else: return 'R'
    if a == 'S':
        if b == 'R': return 'R'
        else: return 'S'
    if a == 'P':
        if b == 'S': return 'S'
        else: return 'P'
    assert False

n, k = list(map(int, input().split()))
s = list(input())
for _ in range(k):
    t = s * 2
    for i in range(n):
        s[i] = win(t[i * 2], t[i * 2 + 1])
print((s[0]))

