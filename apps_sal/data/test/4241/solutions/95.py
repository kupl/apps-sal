from sys import stdin
S = stdin.readline().rstrip()
T = stdin.readline().rstrip()
ls, lt = len(S), len(T)
ans = ls
for i in range(0, ls - lt + 1):
    diff = 0
    for j in range(lt):
        if T[j] != S[i + j]:
            diff += 1
    ans = min(ans, diff)
print(ans)
