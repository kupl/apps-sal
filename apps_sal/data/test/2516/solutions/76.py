from collections import Counter

N, P = list(map(int, input().split()))
S = input()

if P in (2, 5):
    ans = sum(i for i, s in enumerate(S, 1) if not int(s) % P)
else:
    Acc = [0] * (N + 1)
    p10 = 1
    for i, s in enumerate(reversed(S)):
        Acc[N - i - 1] = (Acc[N - i] + p10 * int(s)) % P
        p10 = (p10 * 10) % P
    ans = sum(v * (v - 1) // 2 for v in list(Counter(Acc).values()))
print(ans)

