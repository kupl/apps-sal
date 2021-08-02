N = int(input())
evens = [n for n in range(1, N * N + 1) if n % 2 == 0]
odds = [n for n in range(1, N * N + 1) if n % 2 != 0]
s = 0
t = 0
for i in range(N):
    n_even = max(N // 2 - i, i - N // 2)
    n_odd = N - n_even * 2
    res = []
    for ne in range(n_even):
        res.append(evens[s])
        s += 1
    for no in range(n_odd):
        res.append(odds[t])
        t += 1
    for ne in range(n_even):
        res.append(evens[s])
        s += 1
    print(" ".join(map(str, res)))
