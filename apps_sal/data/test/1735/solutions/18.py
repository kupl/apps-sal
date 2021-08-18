s = '^' + input() + '$'
n = len(s)
N = [*list(range(1, n + 1))]
P = [*list(range(-1, n - 1))]

count = 0

i = 0
while N[i] != n:
    if s[i] == s[N[i]]:
        P[N[N[i]]] = P[i]
        N[P[i]] = N[N[i]]
        i = P[i]
        count += 1
    else:
        i = N[i]

print('Yes' if count % 2 else 'No')
