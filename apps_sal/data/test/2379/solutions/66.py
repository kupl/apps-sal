N, K, C = [int(_) for _ in input().split()]
S = input()
cand = [i + 1 for i, s in enumerate(S) if s == 'o']
F = [[cand[0]]]
for c in cand[1:]:
    if c - F[-1][0] > C:
        F += [[]]
    F[-1] += [c]
if len(F) > K:
    return
B = [[cand[-1]]]
for c in cand[-2::-1]:
    if B[-1][0] - c > C:
        B[-1] = B[-1][::-1]
        B += [[]]
    B[-1] += [c]
B = B[::-1]
B[0] = B[0][::-1]
ans = []
for f, b in zip(F, B):
    if len(f) == 1 or f[1] not in b:
        ans += [f[0]]
print(('\n'.join(map(str, ans))))

