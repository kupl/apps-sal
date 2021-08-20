win = {'R': 'P', 'P': 'S', 'S': 'R'}
(n, k) = list(map(int, input().split()))
S = input()
for _ in range(k):
    t = S + S
    for i in range(n):
        a = t[i * 2]
        b = t[i * 2 + 1]
        S = S[:i] + (b if win[a] == b else a) + S[i + 1:]
print(S[0])
