win = {'R': 'P', 'P': 'S', 'S': 'R'}
n, k = list(map(int, input().split()))
s = t = input()
for _ in range(k):
    t, s = s, t[:n]
    t += t
    for i in range(n):
        a = t[i * 2]
        b = t[i * 2 + 1]
        s = s[:i] + (b if win[a] == b else a) + s[i + 1:]
print((s[0]))
