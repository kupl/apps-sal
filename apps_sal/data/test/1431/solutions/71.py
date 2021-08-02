N = int(input())
A = [0] + list(map(int, input().split()))
Ans = [0] * (N + 1)
for i, a in zip(list(range(N, 0, -1)), A[:0:-1]):
    n = 0
    for aj in Ans[i * 2::i]:
        n ^= aj
    Ans[i] = n ^ a
Ans = [i for i, a in enumerate(Ans[1:], 1) if a]
print((len(Ans)))
print((" ".join(map(str, Ans))))
