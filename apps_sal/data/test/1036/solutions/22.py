def win(a, b):
    w = a
    if a == 'R' and b == 'P':
        w = b
    if a == 'P' and b == 'S':
        w = b
    if a == 'S' and b == 'R':
        w = b
    return w


n, k = list(map(int, input().split()))
S = input()

for _ in range(k):
    t = S + S
    for i in range(n):
        S = S[:i] + win(t[i * 2], t[i * 2 + 1]) + S[i + 1:]
print((S[0]))
