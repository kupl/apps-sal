n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = [ti for ti in input()]
score = {"z": 0, "r": p, "s": r, "p": s}
for i in range(k, n):
    if t[i] == t[i - k]:
        t[i] = "z"
print(sum([score[ti] for ti in t]))
